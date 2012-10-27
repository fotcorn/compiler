import unittest
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser, ParseError

class ParserTest(unittest.TestCase):
    
    def test_brackets_unclosed(self):
        with self.assertRaises(ParseError):
            self.parse('print (5*3')
    
    def test_brackets_unopened(self):
        with self.assertRaises(ParseError):
            self.parse('print 5*3)')
    
    def test_brackets_ok(self):
        self.parse('print (5*3)')
    
    def test_calculate_minus1(self):
        self.parse('print 100 - 10')
    
    def test_calculate_minus2(self):
        self.parse('print (100 - 10)')
    
    def test_calculate_minus3(self):
        self.parse('print (100 - 10) * 5')
        
    def test_calculate_plus(self):
        self.parse('print (100 + 10) * 5')
        
    #def test_calcluate_minus_minus(self):
    #    self.parse('print 100 - - 10')
    
    def parse(self, code):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(code)
        parser = Parser()
        return parser.parse(tokens)
        