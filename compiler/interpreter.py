from compiler.ast import VarDefinition, Identifier, Assignment, Input, Print,\
    Constant, Expression, WhileStart, WhileEnd

class InterpreterError(Exception): pass

class Interpreter():
    
    
    def interpret(self, ast):
        self.vars = {}
        
        ip = 0 # instruction pointer
        
        while True:
            if ip >= len(ast):
                break
            
            instr = ast[ip]
            
            if isinstance(instr, VarDefinition):
                identifier = instr.identifier.identifier
                if identifier in self.vars.keys():
                    raise Exception('Variable %s already defined' % identifier)
                
                if hasattr(instr, 'expression'):
                    value = self.expression(instr.expression)
                else:
                    value = None
                self.vars[identifier] = value
            elif isinstance(instr, Assignment):
                identifier = instr.identifier.identifier
                if not identifier in self.vars.keys():
                    raise Exception('Undefined variable %s' % identifier)
                value = self.expression(instr.expression)
                self.vars[identifier] = value
            elif isinstance(instr, Input):
                identifier = instr.identifier.identifier
                self.vars[identifier] = int(raw_input())
            elif isinstance(instr, Print):
                value = self.expression(instr.expression)
                print value
            elif isinstance(instr, WhileStart):
                if not self.comparision(instr.expression1, instr.expression2, instr.compare_op):
                    i = ip + 1
                    stack = 0
                    while True:
                        if isinstance(ast[i], WhileEnd):
                            if stack == 0:
                                break
                            else:
                                stack -= 1
                        elif isinstance(ast[i], WhileStart):
                            stack += 1
                        i += 1
                        if i == len(ast):
                            raise InterpreterError('while start is last instruction in program')
                    ip = i
            elif isinstance(instr, WhileEnd):
                i = ip - 1
                stack = 0
                while True:
                    if isinstance(ast[i], WhileStart):
                        if stack == 0:
                            break
                        else:
                            stack -= 1
                    elif isinstance(ast[i], WhileEnd):
                        stack += 1
                    i -= 1
                    if i < 0:
                        raise InterpreterError('endwhile without while')
                ip = i - 1
            
            ip += 1
            
    
    def expression(self, expression):
        value = 0
        for term in expression.terms:
            if term.sign == '-':
                value -= self.term(term)
            else:
                value += self.term(term)
        return value
    
    def term(self, term):
        value = None
        for factor in term.factors:
            if isinstance(factor, Constant):
                val = int(factor.constant)
            elif isinstance(factor, Identifier):
                val = self.vars[factor.identifier]
            elif isinstance(factor, Expression):
                val = self.expression(factor)
            if hasattr(factor, 'sign'):
                if factor.sign == '*':
                    value *= val
                else:
                    value /= val
            else:
                value = val
        return value
    
    def comparision(self, expression1, expression2, operator):
        exp1 = self.expression(expression1)
        exp2 = self.expression(expression2)
        
        if operator == '>':
            return exp1 > exp2
        elif operator == '<':
            return exp1 < exp2
        else:
            raise InterpreterError('unsupported comparision operator')
        
        
