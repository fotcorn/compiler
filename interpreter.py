from ast import *


class Interpreter():
    
    
    def interpret(self, ast):
        self.vars = {}
        
        for instr in ast:
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
                if not identifier in vars.keys():
                    raise Exception('Undefined variable %s' % identifier)
                value = self.expression(instr.expression)
                self.vars[identifier] = value
            elif isinstance(instr, Input):
                identifier = instr.identifier.identifier
                self.vars[identifier] = int(raw_input())
            elif isinstance(instr, Print):
                value = self.expression(instr.expression)
                print value
            
            
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
            
            
            
            

        