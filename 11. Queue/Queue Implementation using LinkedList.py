class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        if self.head is None:
            node  = Node(data, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, None)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head == None:
            print("Queue is empty!")
            return None
        else:
            print()
            print(f'{self.head.data} is dequeqe')
            self.head = self.head.next

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_queue()
q.dequeue()
print()
q.print_queue()
        


