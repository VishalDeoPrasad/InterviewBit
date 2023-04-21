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

    def get_length(self):
        temp = self.head
        cnt = 0
        while temp!= None:
            temp = temp.next
            cnt += 1

        print(cnt)


    


ll = LinkedList()
ll.inset_at_front(30)
ll.inset_at_front(20)
ll.inset_at_front(10)
ll.get_length()