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
        
a = LinkedList()
a.append("LAX")
a.append("LGB")
a.append("JFK")
a.printList()
a.prepend("SFO")
a.printList()