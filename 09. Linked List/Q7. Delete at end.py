class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_front(self, data):
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
        curr = 1
        while curr < idx-1:
            temp = temp.next
            curr += 1
        
        node = Node(data, temp.next)
        temp.next = node

    def delete_at_front(self):
        self.head = self.head.next

    def delete_at_end(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

ll = LinkedList()
ll.insert_at_front(100)
ll.insert_at_front(90)
ll.insert_at_front(80)
ll.insert_at_end(110)
ll.insert_at_end(120)
ll.insert_at_end(130)
ll.insert_at_index(95, 3)
ll.insert_at_index(96, 4)
ll.insert_at_index(98, 5)
ll.print_list()
ll.delete_at_front()
ll.print_list()
ll.delete_at_end()
ll.print_list()
