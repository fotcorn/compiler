
class ASTNode(object):
    def __str__(self):
        ret = '<' + self.__class__.__name__ + ': '
        for name, value in self.__dict__.items():
            if isinstance(value, basestring):
                ret += name + "='" + str(value) + "', "
            else:
                ret += name + '=' + str(value) + ', '
        ret = ret[:-2] + '>'
        return ret
    def __repr__(self):
        return self.__str__()
        

class Print(ASTNode): pass
class Input(ASTNode): pass

class VarDefinition(ASTNode): pass
class Assignment(ASTNode): pass

class Constant(ASTNode):
    def __init__(self, constant):
        self.constant = constant
    
class Identifier(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier
        
class Term(ASTNode):
    def __init__(self):
        self.factors = []
        
class Expression(ASTNode):
    def __init__(self):
        self.terms = []

