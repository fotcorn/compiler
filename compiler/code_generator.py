from compiler.ast import Print, Constant, Identifier, Expression

class CodeGeneratorError():
    pass

class CodeGenerator():
    
    TEMP_REGS = ['rcx', 'rsi', 'rdi', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

    def add(self, code):
        self.code += code + '\n'
    
    def boilerplate_start(self):
        self.add('extern printf')
        self.add('global main')
        self.add('SECTION .data')
        self.add('print_format_str: db "%d", 10, 0')
        self.add('SECTION .text')
        self.add('main:')
    
    def boilerplate_end(self):
        self.add('mov rax, 0')
        self.add('ret')
    
    def generate(self, ast):
        self.code = ''
        self.boilerplate_start()
        
        self.current_scope = {}
        self.scope_stack = [self.current_scope]
        
        for line in ast:
            if isinstance(line, Print):
                self.temp_regs = self.TEMP_REGS[::-1]
                self.expression(line.expression)
                self.add('mov rdi, print_format_str')
                self.add('mov rsi, rcx')
                self.add('xor rax, rax')
                self.add('call printf')
        self.boilerplate_end()
        return self.code    
    
    def expression(self, expression):
        """
        calculate expression and save result in rbx
        """
        temp_reg = self.temp_regs.pop()
        
        for i, term in enumerate(expression.terms):
            self.term(term)
            if i == 0:
                self.add('mov %s, rax' % temp_reg)
            elif term.sign == '+':
                self.add('add %s, rax' % temp_reg)
            elif term.sign == '-':
                self.add('sub %s, rax' % temp_reg)
        return temp_reg
        
    def term(self, term):
        for i, factor in enumerate(term.factors):
            if isinstance(factor, Constant):
                if i == 0:
                    self.add('mov rax, %s' % factor.constant)
                elif factor.sign == '*':
                    self.add('mov rdx, %s' % factor.constant)
                    self.add('imul rax, rdx')
                elif factor.sign == '/':
                    self.add('xor rdx, rdx')
                    self.add('mov rbx, %s' % factor.constant)
                    self.add('idiv rbx')
                else:
                    raise CodeGeneratorError('Error in term generation')
            elif isinstance(factor, Identifier):
                pass
            elif isinstance(factor, Expression):
                temp_reg = self.expression(factor)
                self.add('mov rax, %s' % temp_reg)
            
            