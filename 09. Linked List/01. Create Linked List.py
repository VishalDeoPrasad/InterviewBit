class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def inset_at_front(self, data):
        node = Node(data, self.head)
        self.head = node


ll = LinkedList()
ll.inset_at_front(30)
ll.inset_at_front(20)
ll.inset_at_front(10)

