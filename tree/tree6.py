# write the bfs traversion of the tree

import collections

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

def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        makeList(r.left)
        if r.left:
            d[r.data].append(r.left.data)
        makeList(r.right)
        if r.right:
            d[r.data].append(r.right.data)
    return d

def bfs(al):
    queue = collections.deque('g')
    visited = []

    while queue:
        node = queue.popleft()
        visited.append(node)
        [queue.append(x) for x in al[node]]
    print(visited)

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

    d = {}
    aList = makeList(root)
    

    bfs(aList)