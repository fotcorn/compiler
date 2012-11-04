"""

[(1, 'var'), (4, 'a'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'b'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'c'), (5, '='), (3, '3')]
[(4, 'c'), (5, '='), (4, 'c'), (6, '+'), (4, 'a'), (6, '+'), (4, 'b')]
[(2, 'print'), (4, 'a')]

"""
from compiler.symbols import PRINT_KEYWORD, INPUT_KEYWORD, VAR_KEYWORD,\
    IDENTIFIER, EQUALS, PLUS, MINUS, STAR, SLASH, VALUE, LPAREN, RPAREN
from compiler.ast import VarDefinition, Identifier, Print, Input, Assignment,\
    Expression, Term, Constant
    

class ParseError(Exception): pass

class Parser(object):

    def parse(self, tokens):
        self.ast = []
        for token in tokens:
            self.current_line = token
            self.current_pos = 0
            self.line()
        return self.ast
    
    def accept(self, symbol):
        if self.current_pos < len(self.current_line) and self.current_line[self.current_pos][0] == symbol:
            self.current_pos += 1
            return True
        else:
            return False
    
    def expect(self, symbol):
        if self.accept(symbol):
            return True
        else:
            raise ParseError('Excepted Symbol')
        
    def get_value(self):
        return self.current_line[self.current_pos-1][1]
    
    def get_symbol(self):
        if self.current_pos >= len(self.current_line):
            return None
        return self.current_line[self.current_pos][0]
    
    def next_symbol(self):
        self.current_pos += 1
    
    def line(self):
        if self.accept(PRINT_KEYWORD):
            self.ast.append(self.print_call())
        elif self.accept(INPUT_KEYWORD):
            self.ast.append(self.input_call())
        elif self.accept(VAR_KEYWORD):
            self.ast.append(self.var_defintion())
        elif self.accept(IDENTIFIER):
            self.ast.append(self.assignment())
        else:
            raise ParseError('Error parsing line')
        
        if len(self.current_line) != self.current_pos:
            raise ParseError('Not all tokens parsed')
    
    def var_defintion(self):
        self.expect(IDENTIFIER)
        vd = VarDefinition()
        vd.identifier = Identifier(self.get_value())
        if self.accept(EQUALS):
            vd.expression = self.expression()
        return vd
    
    def print_call(self):
        p = Print()
        p.expression = self.expression()
        return p
        
    def input_call(self):
        self.expect(IDENTIFIER)
        i = Input()
        i.identifier = Identifier(self.get_value())
        return i
    
    def assignment(self):
        a = Assignment()
        a.identifier = Identifier(self.get_value())
        self.expect(EQUALS)
        a.expression = self.expression()
        return a
        
    def expression(self):
        exp = Expression()
        sign = '+'
        while True:
            if self.get_symbol() == PLUS:
                self.next_symbol()
            elif self.get_symbol() == MINUS:
                if sign == '+':
                    sign = '-'
                else:
                    sign = '+'
                self.next_symbol()
            else:
                break
        
        term = self.term()
        term.sign = sign
        
        exp.terms.append(term)
        
        while True:
            sign = '+'
            while True:
                if self.get_symbol() == PLUS:
                    pass
                elif self.get_symbol() == MINUS:
                    if sign == '+':
                        sign = '-'
                    else:
                        sign = '+'
                elif self.get_symbol() == VALUE or self.get_symbol() == IDENTIFIER or self.get_symbol() == LPAREN:
                    break
                else:
                    return exp
                self.next_symbol()

            term = self.term()
            term.sign = sign
            exp.terms.append(term)
    
    def term(self):
        term = Term()
        factor = self.factor()
        term.factors.append(factor)
        
        while True:
            if self.get_symbol() == STAR:
                sign = '*'
            elif self.get_symbol() == SLASH:
                sign = '/'
            else:
                break
            self.next_symbol()
            factor = self.factor()
            factor.sign = sign
            term.factors.append(factor)
        return term
    
    def factor(self):
        if self.accept(VALUE):
            return Constant(self.get_value())
        elif self.accept(IDENTIFIER):
            return Identifier(self.get_value())
        elif self.accept(LPAREN):
            exp = self.expression()
            self.expect(RPAREN)
            return exp
        else:
            raise ParseError('Error: bad factor')

