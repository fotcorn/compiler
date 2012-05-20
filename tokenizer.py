import re
from symbols import *


STATE_IDENTIFIER = 1
STATE_DIGIT = 2

class Tokenizer(object):
    def tokenize(self, string):
        tokens = []
        for line in string.split('\n'):
            line = line.strip()
            if len(line) == 0:
                continue
            
            self.current_line = []
            self.parse_line(line)
            if len(self.current_line) > 0:
                tokens.append(self.current_line)
        return tokens
    
    def parse_line(self, line):
        self.state = None
        self.current_literal = ''
        for char in line:
            if re.match(r'\s', char):
                self.close_literal()
            elif re.match(r'[A-Za-z]', char):
                self.state = STATE_IDENTIFIER
                self.current_literal += char
            elif re.match(r'\d', char):
                self.state = STATE_DIGIT
                self.current_literal += char
            elif char == '=':
                self.close_literal()
                self.current_line.append((EQUALS,))
            elif char == '+':
                self.close_literal()
                self.current_line.append((PLUS,))
            elif char == '-':
                self.close_literal()
                self.current_line.append((MINUS,))
            elif char == '*':
                self.close_literal()
                self.current_line.append((STAR,))
            elif char == '/':
                self.close_literal()
                self.current_line.append((SLASH,))
            elif char == '(':
                self.close_literal()
                self.current_line.append((LPAREN,))
            elif char == ')':
                self.close_literal()
                self.current_line.append((RPAREN,))
            elif char == '#':
                self.close_literal()
                return
        self.close_literal()
            
    
    def close_literal(self):
        if self.state == STATE_IDENTIFIER:
            if self.current_literal == 'print':
                self.current_line.append((PRINT_KEYWORD,))
            elif self.current_literal == 'var':
                self.current_line.append((VAR_KEYWORD,))
            elif self.current_literal == 'input':
                self.current_line.append((INPUT_KEYWORD,))
            else:
                self.current_line.append((IDENTIFIER, self.current_literal))
            self.current_literal = ''
            self.state = None
        elif self.state == STATE_DIGIT:
            self.current_line.append((VALUE, self.current_literal))
            self.current_literal = ''
            self.state = None

