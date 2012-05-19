from tokenizer import Tokenizer
from parser import Parser
from symbols import TOKENS

f = open('examples/vars', 'r')
code = f.read()
f.close()

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(code)

#parser = Parser()
#ast = parser.parse(tokens)

for line in tokens:
    print
    for token in line:
        print TOKENS[token[0]]