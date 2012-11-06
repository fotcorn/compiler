from compiler.ast import Print, Constant


class CodeGenerator():
    
    def boilerplate_start(self):
        self.code += """
        extern printf
        global main
        
        SECTION .data
        
        print_format_str: db "%d", 10, 0
        
        SECTION .text
        main:
        """
    
    def boilerplate_end(self):
        self.code += """
        mov rax, 0
        ret
        """
    
    def generate(self, ast):
        self.code = ''
        self.boilerplate_start()
        for line in ast:
            if isinstance(line, Print):
                self.expression(line.expression)
                self.code += """
                mov rdi, print_format_str
                mov rsi, rax
                mov rax, 0
                call printf
                """
        self.boilerplate_end()
        return self.code    
    
    def expression(self, expression):
        """
        calculate expression and save result in rax
        """
        for term in expression.terms:
            self.term(term)
    
    def term(self, term):
        for factor in term.factors:
            if isinstance(factor, Constant):
                self.code += 'mov rax, ' + factor.constant + '\n'
            
            