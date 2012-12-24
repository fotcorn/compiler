
class Print(object):
    def __init__(self):
        self.expression = None

class Leaf(object):
    def __init__(self, parent):
        self.parent = parent

class NumberLeaf(Leaf):
    def __init__(self, parent=None, value=None):
        super(NumberLeaf, self).__init__(parent)
        self.value = value

class Node(object):
    def __init__(self, parent=None, operator=None):
        self.parent = parent
        self.operator = operator
        self.left_child = None
        self.right_child = None
