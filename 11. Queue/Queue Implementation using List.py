class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} is Inserted:")
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
        else:
            self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def print_queue(self):
        if self.isEmpty():
            print("Queue is empty:")
        else:
            print(self.queue, end=" ")

q = Queue()
q.enqueue(10)
q.print_queue()
q.dequeue()
q.dequeue()
q.print_queue()