class Stack:
    def __init__(self, limit=10):
        self.stack_box = []
        self.limit = limit

    def Push(self, data):
        if len(self.stack_box) >= self.limit:
            print("Stack is Overflow!")
            return None
        else:
            self.stack_box.append(data)
            print(f"{data} : push to stack")

    def Pop(self):
        if len(self.stack_box) <= 0:
            print("Stack is Underflow!")
            return None
        else:
            return self.stack_box.pop() 
        
    def IsEmpty(self):
        if len(self.stack_box) <= 0:
            print("Stack is Empty!")
            return None
        else:
            print("Stack is not Empty!")
            return len(self.stack_box)
        
    def stack_size(self):
        print(len(self.stack_box))
    
    def print_stack(self):
        print(self.stack_box)
    
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.print_stack()
s.Pop()
s.Pop()
s.print_stack()
s.IsEmpty()
s.stack_size()
