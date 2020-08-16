class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def printTree(self,Traversal_type):
        if(Traversal_type=="preorder"):
            return self.preorder(tree.root,"")
        

    def preorder(self,start,traversal):
        if start:
            traversal+=(str(start.data) + " - ")
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

#setting up tree
tree = BinaryTree("F")
tree.root.left = Node("B")
tree.root.right = Node("G")
tree.root.left.left = Node("A")
tree.root.left.right = Node("D")
tree.root.left.right.left = Node("C")
tree.root.left.right.right = Node("E")
tree.root.right.right = Node("I")
tree.root.right.right.left = Node("H")
    
print(tree.printTree("preorder"))

