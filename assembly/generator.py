import sys

print 'int main() {'

for i in range(25, -1, -1):
    print 'int ' + chr(i+97) + ' = ' + str(i) + ';'
    
sys.stdout.write('return ')
for i in range(0, 16):
    sys.stdout.write('(29 / %s) * (' % chr(i+97))

sys.stdout.write(')' * 16)


print
print '}'
