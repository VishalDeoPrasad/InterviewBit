class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, limit=10):
        self.head = None
        self.limit = limit
    
    def push(self, data):
        if self.get_length() >= self.limit:
            print("Stack Overflow, can not push data:")
            return None
        else:
            node = Node(data, self.head)
            print(f'{data} is Pushed:')
            self.head = node

    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        temp = self.head.data
        self.head = self.head.next
        print(f'{temp} is Poped')

    def isEmpty(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        else:
            print("Stack is not empty!")

    def peak(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        else:
            print(self.head.data)

    def get_length(self):
        temp = self.head
        cnt = 0
        while temp:
            temp = temp.next
            cnt += 1
        return cnt

    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
s.push(90)
s.push(100)
s.push(110)
s.push(120)
