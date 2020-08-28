arr = [1,2,3,4,5]

class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.cur_len = 0

    def insert(self,data):
        self.heap.append(data)
        self.cur_len+=1
        i = self.cur_len
        while i//2>0:
            if self.heap[i//2]<self.heap[i]:
                self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
            i//=2

    def delete(self):
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        self.cur_len -=1
        i = 1
        while i*2<=self.cur_len:
            if (i*2)+1>self.cur_len:
                mc = i*2
            elif(self.heap[i*2]>self.heap[(i*2)+1]):
                mc = i*2
            else:
                mc = (i*2)+1
            if(self.heap[mc]>self.heap[i]):
                self.heap[mc],self.heap[i] = self.heap[i],self.heap[mc]
            i*=2



    def printHeap(self):
        print(self.heap[1:])
        
mh = MaxHeap()
mh.insert(3)
mh.insert(5)
mh.insert(2)
mh.insert(10)
mh.insert(20)
mh.insert(1)
mh.insert(4)
mh.printHeap()
mh.delete()
mh.printHeap()

