import unittest
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.optimizer import Optimizer



class OptimizerTests(unittest.TestCase):
    
    def optimize(self, code, expected):
        tokenizer1 = Tokenizer()
        tokenizer2 = Tokenizer()
        tokens1 = tokenizer1.tokenize('var i = ' + code)
        tokens2 = tokenizer2.tokenize('var i = ' + expected)
        parser1 = Parser()
        parser2 = Parser()
        ast1 = parser1.parse(tokens1)
        ast2 = parser2.parse(tokens2)
        optimizer = Optimizer()
        optimizer.optimize(ast1)
        self.assertEqual(ast1, ast2)
    
    def test_simple1(self):
        self.optimize('(5+5)', '5+5')
    
    def test_simple2(self):
        self.optimize('((5+5))', '5+5')
        
    def test_simple3(self):
        self.optimize('((5))', '5')
        
    
    def test_parens1(self):
        self.optimize('(5+5)*5', '(5+5)*5')
    
    def test_parens2(self):
        self.optimize('5+(5*5)', '5+5*5')


