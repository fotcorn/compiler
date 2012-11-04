import unittest
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser, ParseError
from compiler.interpreter import Interpreter

class CalculationTests(unittest.TestCase):
    
    def interpret_calculation(self, calculation, expected=0):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize('var i = ' + calculation)
        parser = Parser()
        ast =  parser.parse(tokens)
        interpreter = Interpreter()
        interpreter.interpret(ast)
        self.assertEqual(interpreter.vars['i'], expected)
    
    # brackets
    def test_brackets_unclosed(self):
        with self.assertRaises(ParseError):
            self.interpret_calculation('(5*3')
    
    def test_brackets_unopened(self):
        with self.assertRaises(ParseError):
            self.interpret_calculation('5*3)')
    
    def test_brackets_ok(self):
        self.interpret_calculation('(5*3)', 15)
        
    def test_brackets_prefix(self):
        self.interpret_calculation('-(9+5)', -14)
    
    # calculations
    def test_calculate_minus1(self):
        self.interpret_calculation('100 - 10', 90)
    
    def test_calculate_minus2(self):
        self.interpret_calculation('(100 - 10)', 90)
    
    def test_calculate_minus3(self):
        self.interpret_calculation('(100 - 10) * 5', 450)
    
    def test_calculate_plus(self):
        self.interpret_calculation('(100 + 10) * 5', 550)
    
    def test_calculate_minus_minus(self):
        self.interpret_calculation('10 - - 5', 15)
    
    def test_calculate_minus_plus1(self):
        self.interpret_calculation('- + 5', -5)
    
    def test_calculate_minus_plus2(self):
        self.interpret_calculation('10 - + 5', 5)
    
    def test_calculate_plus_plus(self):
        self.interpret_calculation('10 + + 5', 15)
    
    def test_calculate_plus_minus(self):
        self.interpret_calculation('10 + - 5', 5)
    

