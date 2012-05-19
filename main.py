from tokenizer import tokenize
from symbols import TOKENS
from parser import Parser

f = open('examples/vars', 'r')
code = f.read()
f.close()


tokens = tokenize(code)

parser = Parser()
parser.parse(tokens)