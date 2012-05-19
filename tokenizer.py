import re

TOKEN_REGEX = {
    1: 'var',
    2: 'print',
    3: 'input',
    4: '\d+',
    5: '[[A-Za-z]+',
    6: '=',
    7: '\\+',
}

def tokenize(string):
    tokens = []
    for line in string.split('\n'):
        if len(line.strip()) == 0:
            continue
        
        current_line = []
        
        for token in re.split('\s+', line):
            if len(token) == 0:
                continue
            
            found = False
            for token_id, regex in TOKEN_REGEX.items():
                if re.match(regex, token):
                    current_line.append((token_id, token))
                    found = True
                    break
            if found == False:
                raise Exception('Unknown token %s', token)
    
        tokens.append(current_line)
    return tokens

