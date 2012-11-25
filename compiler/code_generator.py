from compiler.ast import Print, Constant, Identifier, Expression, VarDefinition,\
    Assignment, Input, IfEnd, IfStart, WhileEnd, WhileStart

class CodeGeneratorError():
    pass

class CodeGenerator():
    
    TEMP_REGS = ['rcx', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

    def add(self, code):
        self.code += code + '\n'
    
    def boilerplate_start(self):
        self.add('extern printf') # define external function
        self.add('global main') # export symbol main
        self.add('SECTION .data') # start of static data section
        self.add('print_format_str: db "%d", 10, 0') # save printf format string for integers "%d\n\0"
        self.add('SECTION .text') # start of program code section
        self.add('main:') # main label
        self.add('push rbp') # push old base pointer
        self.add('mov rbp, rsp') # set up stack frame
    
    def boilerplate_end(self):
        self.add('pop rbp') # destroy stack frame
        self.add('mov rax, 0') # set program return type to 0
        self.add('ret') # return to operating system
    
    def generate(self, ast):
        self.code = ''
        self.boilerplate_start()
        
        self.current_scope = {}
        self.scope_stack = [self.current_scope]
                
        for instr in ast:
            if isinstance(instr, Print):
                temp_reg = self.expression(instr.expression, True)
                self.add('mov rdi, print_format_str')
                self.add('mov rsi, %s' % temp_reg)
                self.add('xor rax, rax')
                self.add('call printf')
            elif isinstance(instr, VarDefinition):
                identifier = instr.identifier.identifier
                
                if identifier in self.current_scope:
                    raise CodeGeneratorError('variable %s already definded', identifier)
                
                # mov [rbp-8], 5
                stack_position = (len(self.current_scope) + 1)  * 8
                self.current_scope[identifier] = stack_position
                
                if hasattr(instr, 'expression'):
                    temp_reg = self.expression(instr.expression, True)
                    self.add('mov qword [rbp-%s], %s' % (stack_position, temp_reg))
                else:
                    self.add('mov qword [rbp-%s], 0' % stack_position)
            elif isinstance(instr, Assignment):
                identifier = instr.identifier.identifier
                try:
                    stack_position = self.current_scope[identifier]
                except KeyError:
                    raise CodeGeneratorError('variable %s not declared', identifier)
                temp_reg = self.expression(instr.expression, True)
                self.add('mov qword [rbp-%s], %s' % (stack_position, temp_reg))
                
            
            elif isinstance(instr, Input):
                raise CodeGeneratorError('not implemented: Input')
            elif isinstance(instr, WhileStart):
                raise CodeGeneratorError('not implemented: WhileStart')
            elif isinstance(instr, WhileEnd):
                raise CodeGeneratorError('not implemented: WhileEnd')
            elif isinstance(instr, IfStart):
                raise CodeGeneratorError('not implemented: IfStart')
            elif isinstance(instr, IfEnd):
                raise CodeGeneratorError('not implemented: IfEnd')
            else:
                raise CodeGeneratorError('unknown instruction: %s' % instr)
                
        self.boilerplate_end()
        return self.code    
    
    def expression(self, expression, toplevel=False):
        """
        calculate expression and save result in rbx
        """
        if toplevel:
            self.temp_regs = self.TEMP_REGS[::-1]
        
        temp_reg = self.temp_regs.pop()
        
        for i, term in enumerate(expression.terms):
            term_reg = self.term(term)
            if i == 0:
                self.add('mov %s, %s' % (temp_reg, term_reg))
            elif term.sign == '+':
                self.add('add %s, %s' % (temp_reg, term_reg))
            elif term.sign == '-':
                self.add('sub %s, %s' % (temp_reg, term_reg))
        return temp_reg
        
    def term(self, term):
        temp_reg = self.temp_regs.pop()
        for i, factor in enumerate(term.factors):
            if isinstance(factor, Constant):
                source = factor.constant
            elif isinstance(factor, Identifier):
                try:
                    stack_position = self.current_scope[factor.identifier]
                except KeyError:
                    raise CodeGeneratorError('use of undefined variable %s', factor.identifier)
                source = 'qword [rbp-%s]' % stack_position
            elif isinstance(factor, Expression):
                source = self.expression(factor)
            
            if i == 0:
                self.add('mov %s, %s' % (temp_reg, source))
            elif factor.sign == '*':
                self.add('mov rdx, %s' % source)
                self.add('imul %s, rdx' % temp_reg)
            elif factor.sign == '/':
                self.add('mov rax, %s' % temp_reg)
                self.add('xor rdx, rdx')
                self.add('mov rbx, %s' % source)
                self.add('idiv rbx')
                self.add('mov %s, rax' % temp_reg)
        return temp_reg
