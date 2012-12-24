import sys

VAR_KEYWORD = 1
PRINT_KEYWORD = 2
INPUT_KEYWORD = 3

WHILE_KEYWORD = 15
ENDWHILE_KEYWORD = 16
IF_KEYWORD = 17
ENDIF_KEYWORD = 18

VALUE = 4
IDENTIFIER = 5

EQUALS = 6
PLUS = 7
MINUS = 8
STAR = 9
SLASH = 10

LPAREN = 11
RPAREN = 12

LESS_THAN = 13
GREATER_THAN = 14

TOKENS = {
    1: 'VAR_KEYWORD',
    2: 'PRINT_KEYWORD',
    3: 'INPUT',
    4: 'VALUE',
    5: 'IDENTIFIER',
    6: 'EQUALS',
    7: 'PLUS',
    8: 'MINUS',
    9: 'STAR',
    10: 'SLASH',
    11: 'LPAREN',
    12: 'RPAREN',
    13: 'LESS_THAN',
    14: 'GREATER_THAN',
    15: 'WHILE_KEYWORD',
    16: 'ENDWHILE_KEYWORD',
    17: 'IF_KEYWORD',
    18: 'ENDIF_KEYWORD',
}

def print_line(line):
    for token in line:
        if len(token) == 2:
            sys.stdout.write('%s ' % token[1])
        else:
            sys.stdout.write('%s ' % TOKENS[token[0]])
    sys.stdout.write('\n')
    
    
