from compiler.ast import VarDefinition, Assignment, Print, Expression


class Optimizer():
    def optimize(self, ast):
        for instr in ast:
            if isinstance(instr, VarDefinition):
                if hasattr(instr, 'expression'):
                    self.expression(instr.expression)

            elif isinstance(instr, Assignment):
                self.expression(instr.expression)

            elif isinstance(instr, Print):
                self.expression(instr.expression)
    
    def expression(self, expression):
        optimized_terms = []
        for term in expression.terms:
            optimized_terms.extend(self.term(term))
        expression.terms = optimized_terms
    
    def term(self, term):
        if len(term.factors) == 1 and isinstance(term.factors[0], Expression):
            terms = term.factors[0].terms
            
            optimized_terms = []
            for term in terms:
                optimized_terms.extend(self.term(term))
            return optimized_terms
        else:
            for factor in term.factors:
                if isinstance(factor, Expression):
                    self.expression(factor)
                    
            return [term]
