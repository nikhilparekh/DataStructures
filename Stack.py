class Stack:
    def __init__(self):
        self.arr = []

    def push(self,element):
        self.arr.append(element)
    
    def pop(self):
        return self.arr.pop()
    
    def peek(self):
        return self.arr[len(self.arr)-1]
    
    def clear(self):
        self.arr.clear()

    def view(self):
        return self.arr
    
    def isEmpty(self):
        return self.arr == []
    
    def size(self):
        return len(self.arr)
    
s = Stack()
s.push(10)
s.push(5)
print(s.view())
s.pop()
print(s.isEmpty())
print(s.peek())
print(s.view())