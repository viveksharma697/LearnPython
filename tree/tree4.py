# PreOrder Traversal of a binary tree

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# defining a recursive insert()
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def postOrderPrint(r):
    if r is None:
        return
    else:
        postOrderPrint(r.left)
        postOrderPrint(r.right)
        print(r.data, end=' ')
if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('k')
    root.insert('j')
    root.insert('l')

postOrderPrint(root)