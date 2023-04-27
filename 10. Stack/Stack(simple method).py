class Stack:
    def __init__(self):
        self.stack = []

    def Push(self, data):
        self.stack.append(data)
    
    def Pop(self):
        data = self.stack.pop()
        return data
    
    def print_stack(self):
        print(self.stack)
    
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.Push(50)
s.print_stack()
s.Pop()
s.print_stack()
