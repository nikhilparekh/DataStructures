class Deque(object):
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return self.deque == []
    
    def addRear(self,element):
        self.deque.insert(0,element)
    
    def addFront(self,element):
        self.deque.append(element)

    def removeFront(self):
        self.deque.pop()

    def removeRear(self):
        self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def view(self):
        return self.deque

d = Deque()

d.addRear("Hello")
d.addFront("World!")
print(d.view())
d.removeRear()
print(d.view())