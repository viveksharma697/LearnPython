# insert a node in BST

class Bstnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Bstnode(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Bstnode(data)

def in_order_traversal(self):
    elements = []

    if self.left:
        elements



        
        