class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        
        node = Node(data, None)
        temp.next = node
    
    def insert_at_index(self, data, idx):
        temp = self.head
        cnt = 1
        while cnt < idx-1:
            temp = temp.next
            cnt += 1
        node = Node(25, temp.next)
        temp.next = node
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
       
ll = LinkedList()
ll.insert_at_begining(30)
ll.insert_at_begining(20)
ll.insert_at_begining(10)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.insert_at_index(25, 3)
ll.print_list()
