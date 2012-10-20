import unittest
from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.interpreter import Interpreter

class InterpreterTest(unittest.TestCase):
    
    def interpret_calculation(self, calculation):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize('var i = ' + calculation)
        parser = Parser()
        ast =  parser.parse(tokens)
        interpreter = Interpreter()
        interpreter.interpret(ast)
        return interpreter.vars['i']
    
    def test_calculate_minus_minus(self):
        self.assertEqual(self.interpret_calculation('10 - - 5'), 15)
    
    def test_calculate_minus_plus(self):
        self.assertEqual(self.interpret_calculation('10 - + 5'), 5)
        
    def test_calculate_plus_plus(self):
        self.assertEqual(self.interpret_calculation('10 + + 5'), 15)
        
    def test_calculate_plus_minus(self):
        self.assertEqual(self.interpret_calculation('10 + - 5'), 5)
    
