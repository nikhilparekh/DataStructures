class Node(object):
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self,data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)

        if(self.head is None):
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def insert(self,prev,data):
        if not prev:
            print("No Node with {} Found".format(prev))
            return
        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node

    def delete(self,element):
        cur_node = self.head
        
        if cur_node and cur_node.data == element:
            self.head = cur_node.next
            cur_node = None
        
        while cur_node and cur_node.data!=element:
            prev_node = cur_node
            cur_node = cur_node.next
        
        if cur_node == None:
            return
        prev_node.next = cur_node.next
        cur_node = None
    
    def del_position(self,index):
        cur_node = self.head
        if(index==0):
            self.head = cur_node.next
            cur_node = None
        else:
            for i in range(index):
                prev_node = cur_node
                cur_node = cur_node.next
            prev_node.next = cur_node.next         
            cur_node = None  

    # def swap(self,element1, element2):
    #     prev1 = None
    #     prev2 = None
    #     cur1 = self.head
    #     cur2 = self.head
    #     while(cur1 and cur1.data!=element1):
    #         prev1 = cur1
    #         cur1 = cur1.next
    #     while(cur2 and cur2.data!=element2):
    #         prev2 = cur2
    #         cur2 = cur2.next

    #     if not cur1 or not cur2:
    #         return
    #     if prev1:
    #         prev1.next = cur2
    #     cur2.next = cur1.next
    #     prev2.next = cur1
    #     cur1.next = 

# A -> B -> C -> D -> 0
# D -> C -> B -> A -> 0

    def rev(self):
        prev = None
        cur_node = self.head
        while cur_node: #eg : cur_node = B
            nxt = cur_node.next #nxt = C
            cur_node.next = prev # B -> A
            prev = cur_node # prev = B
            cur_node = nxt # cur_node = C
        self.head = prev
        
            




        
a = LinkedList()
a.append("LAX")
a.append("LGB")
a.append("JFK")
a.prepend("SFO")
a.delete("LON")
a.printList()
