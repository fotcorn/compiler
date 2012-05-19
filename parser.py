from symbols import *
from ast import *

"""

[(1, 'var'), (4, 'a'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'b'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'c'), (5, '='), (3, '3')]
[(4, 'c'), (5, '='), (4, 'c'), (6, '+'), (4, 'a'), (6, '+'), (4, 'b')]
[(2, 'print'), (4, 'a')]

"""

class Parser(object):

    def parse(self, tokens):
        self.ast = []
        for token in tokens:
            self.current_line = token
            self.current_pos = 0
            try:
                self.line()
            except Exception, ex:
                print 'Error "%s" on line %s' % (ex, str(token))
                print 'On token %s' % str(token[self.current_pos])
                return
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
            raise Exception('Excepted Symbol')
        
    def get_value(self):
        return self.current_line[self.current_pos-1][1]
    
    def line(self):
        if self.accept(PRINT_KEYWORD):
            self.ast.append(self.print_call())
        elif self.accept(INPUT_KEYWORD):
            self.ast.append(self.input_call())
        elif self.accept(VAR_KEYWORD):
            self.ast.append(self.var_defintion())
        elif self.accept(IDENTIFIER):
            self.ast.append(self.assigment())
        else:
            raise Exception('Error parsing line')
    
    def var_defintion(self):
        self.expect(IDENTIFIER)
        vd = VarDefinition()
        vd.identifier = Identifier(self.get_value())
        if self.accept(EQUALS):
            vd.term = self.term()
        return vd
    
    def print_call(self):
        p = Print()
        p.term = self.term()
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
        a.term = self.term()
        return a
        
    # general term returning value, ex: 5 + 4, a + b + 3
    def term(self):
        factor1 = self.factor()
        t = None
        if self.accept(PLUS):
            t = Plus()
            t.factor1 = factor1
            t.factor2 = self.term()
        else:
            t = Term()
            t.factor1 = factor1
        return t
    
    def factor(self):
        if self.accept(VALUE):
            return Constant(self.get_value())
        elif self.accept(IDENTIFIER):
            return Identifier(self.get_value())
        else:
            raise Exception('Error: bad factor')
    