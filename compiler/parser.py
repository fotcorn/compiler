"""

[(1, 'var'), (4, 'a'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'b'), (5, '='), (3, '5')]
[(1, 'var'), (4, 'c'), (5, '='), (3, '3')]
[(4, 'c'), (5, '='), (4, 'c'), (6, '+'), (4, 'a'), (6, '+'), (4, 'b')]
[(2, 'print'), (4, 'a')]

"""
from compiler.symbols import PRINT_KEYWORD, INPUT_KEYWORD, VAR_KEYWORD,\
    IDENTIFIER, EQUALS, PLUS, MINUS, STAR, SLASH, VALUE, LPAREN, RPAREN,\
    IF_KEYWORD, ENDIF_KEYWORD, WHILE_KEYWORD, ENDWHILE_KEYWORD, LESS_THAN,\
    GREATER_THAN, print_line
    
from compiler.ast import Node, NumberLeaf

class ParseError(Exception): pass

class Parser(object):

    def parse(self, tokens):
        self.ast = []
        for token in tokens:
            self.current_line = token
            
            if self.current_line[0][0] == PRINT_KEYWORD:
                self.expression()
                print self.node
                
    
    def expression(self):
        self.node = Node()
        for i in range(1, len(self.current_line)):
            token = self.current_line[i]
            if token[0] == VALUE:
                if self.node.left_child == None:
                    self.node.left_child = NumberLeaf(parent=self.node, value=token[1])
                elif self.node.right_child == None:
                    self.node.right_child = NumberLeaf(parent=self.node, value=token[1])
                else:
                    raise ParseError('both child already contain a value')
            elif token[0] == PLUS:
                self.set_operator('+')
            elif token[0] == STAR:
                self.set_operator('*')
    
    def set_operator(self, operator):
        if self.node.operator == None:
            self.node.operator = operator
        else:
            new_node = Node(parent=self.node, operator=operator)
            new_node.left_child = self.node
            self.node = new_node
            
            




