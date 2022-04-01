# reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


strr = "We will conquere COVID-19"
strl = list(strr)

s = Stack()
for i in strl:
    s.push(i)

s.pop()
