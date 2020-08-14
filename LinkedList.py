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
        cur_node.next = None
    
        
        
a = LinkedList()
a.append("LAX")
a.append("LGB")
a.append("JFK")
a.prepend("SFO")
a.insert(a.head.next,"MSO")
a.delete("LON")
a.printList()
