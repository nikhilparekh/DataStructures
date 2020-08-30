class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)
        
    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data,cur_node.left)
        elif(data>cur_node.data):
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("The Node Already Exists")
    
    def find(self,data):
        if self.root:
            found = self._find(data,self.root)
            if found:
                return True
        else:
            return None
    
    def _find(self,data,cur_node):
        if data<cur_node.data:
             self._find(data,cur_node.left)
        elif data > cur_node.data:
             self._find(data,cur_node.right)
        elif data == cur_node.data:
            return True
        else:
            return False            
        

bst = BinarySearchTree()
bst.insert(5)
bst.insert(10)
bst.insert(8)
print(bst.find(8))
# bst.search(2,bst.root)


