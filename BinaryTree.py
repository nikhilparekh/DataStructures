class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        if self.is_empty():
            return
        return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
        
    def size(self):
        return len(self.items)
    



class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def printTree(self,Traversal_type):
        if(Traversal_type=="preorder"):
            return self.preorder(tree.root,"")
        elif(Traversal_type=='inorder'):
            return self.inorder(tree.root,"")
        elif(Traversal_type=='postorder'):
            return self.postorder(tree.root,"")
        elif(Traversal_type=="levelorder"):
            return self.levelorder(tree.root)

    def preorder(self,start,traversal):
        if start:
            traversal+=(str(start.data) + " - ")
            traversal = self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self,start,traversal):
        if start:
            traversal = self.inorder(start.left,traversal)
            traversal+=(str(start.data)+" - ")
            traversal = self.inorder(start.right,traversal)
        return traversal
    
    def postorder(self,start,traversal):
        if start:
            traversal = self.postorder(start.left,traversal)
            traversal = self.postorder(start.right,traversal)
            traversal += (str(start.data)+" - ")
        return traversal

    def levelorder(self,start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while(queue.size()>0):
            traversal+=(str(queue.peek())+" - ")
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
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
print(tree.printTree("inorder"))
print(tree.printTree("postorder"))
print(tree.printTree("levelorder"))
