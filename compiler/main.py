#import sys

from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.interpreter import Interpreter
#from compiler.symbols import TOKENS

f = open('../examples/if', 'r')
code = f.read()
f.close()

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(code)

"""
for line in tokens:
    for token in line:
        sys.stdout.write(TOKENS[token[0]])
        if len(token) == 2:
            sys.stdout.write('(%s)' % token[1])
        sys.stdout.write(' ')
    print
"""

parser = Parser()
ast = parser.parse(tokens)

"""
for a in ast:
    print a
"""

interpreter = Interpreter()
interpreter.interpret(ast)