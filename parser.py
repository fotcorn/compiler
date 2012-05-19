from symbols import *

"""

[(1, 'var'), (4, 'a'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'b'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'c'), (5, '='), (3, '3')]
[(4, 'c'), (5, '='), (4, 'c'), (6, '+'), (4, 'a'), (6, '+'), (4, 'b')]
[(2, 'print'), (4, 'a')]

"""

class Parser(object):

    def parse(self, tokens):
        for token in tokens:
            self.current_line = token
            self.current_pos = 0
            try:
                self.line()
            except Exception, ex:
                print 'Error "%s" on line %s' % (ex, str(token))
                print 'On token %s' % str(token[self.current_pos])
                return
                
    
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
    
    def line(self):
        if self.accept(PRINT_KEYWORD):
            self.print_call()
        elif self.accept(INPUT_KEYWORD):
            self.input_call()
        elif self.accept(VAR_KEYWORD):
            self.var_defintion()
        elif self.accept(IDENTIFIER):
            self.assigment()
        else:
            raise Exception('Error parsing line')
    
    def var_defintion(self):
        self.expect(IDENTIFIER)
        
        if self.accept(EQUALS):
            self.term()
            print 'Variable definition with initialisation'
        else:
            print 'Variable definition without initialisation'
    
    def print_call(self):
        print 'print call'
        self.term()
        
    def input_call(self):
        print 'input call'
        self.expect(IDENTIFIER)
    
    def assigment(self):
        self.expect(EQUALS)
        self.term()
    
    # general term returning value, ex: 5 + 4, a + b + 3
    def term(self):
        self.factor()
        if self.accept(PLUS):
            print 'PLUS'
            self.term()
    
    def factor(self):
        if self.accept(VALUE):
            print 'Factor is number'
        elif self.accept(IDENTIFIER):
            print 'Factor is identifier'
        else:
            raise Exception('Error: bad factor')
    