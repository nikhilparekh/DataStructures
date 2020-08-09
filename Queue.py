class Queue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,element):
        self.queue.insert(0,element)

    def dequeue(self):
        self.queue.pop()

    def size(self):
        return len(self.queue)

    def view(self):
        return self.queue

q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
print(q.view())
q.dequeue()
print(q.size())
print(q.view())