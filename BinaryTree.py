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

class Stack(object):
    def __init__(self):
        self.arr =[]
    
    def push(self,data):
        self.arr.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.pop()
    
    def peek(self):
        return self.arr[-1].value

    def size(self):
        return len(self.arr)
    
    def is_empty(self):
        self.arr == []
    

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
            return self.preorder(self.root,"")
        elif(Traversal_type=='inorder'):
            return self.inorder(self.root,"")
        elif(Traversal_type=='postorder'):
            return self.postorder(self.root,"")
        elif(Traversal_type=="levelorder"):
            return self.levelorder(self.root)
        elif(Traversal_type=="it_inorder"):
            return self.it_inorder(self.root)
        elif(Traversal_type=='it_preorder'):
            return self.it_preoder(self.root)

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

    def it_preoder(self,start):
        stack = []
        res = []
        while True:
            if start:
                stack.insert(0,start)
                # print(stack[0].data)
                start = start.left
            elif not stack:
                break
            else:
                temp = stack.pop()
                res.append(temp.data)
                start = temp.right
            
        return res

    def it_inorder(self,start):
        stack = []
        # stack.append(start)
        res = []
        while True:
            if start:
                stack.append(start)
                start = start.left
                # print("1")
            elif not stack:
                break
            else:
                temp = stack.pop()
                res.append(temp.data)
                start = temp.right
                # stack.append(start)
            
        return res



    def reverseorder(self,start):
        stack = Stack()
        stack.push(start)
        if start.left:
            self.reverseorder(start.left)
        if start.right:
            self.reverseorder(start.right)

    def insertLeft(self,newNode):
        start = self.root
        t = Node(newNode)
        if(start.left==None):
            start.left = t
        else:
            temp = start.left
            while temp!=None:
                temp = temp.left
            temp = t

    def insertRight(self,newNode):
        t = Node(newNode)
        start = self.root
        if start.right is None:
            start.right = t
        else:
            # temp = start.right
            while start!=None:
                start = start.right
            start = t

    def height(self,node):
        if node == None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        # print(left_height,right_height)
        
        return 1+max(left_height,right_height)

    # def size(self,node):
    #     if node == None:
    #         return 0
    #     stack = []
    #     stack.append(node)
    #     total = 1
    #     while(len(stack)>0):
    #         if node.left:
    #             node = node.left
    #             total+=1
    #         if node.ri

    

                





#setting up tree
# tree = BinaryTree("F")
# # tree.root.left = Node("B")
# tree.insertLeft("B")
# # tree.root.right = Node("G")
# tree.insertRight("G")
# tree.root.left.left = Node("A")
# tree.root.left.right = Node("D")
# tree.root.left.right.left = Node("C")
# tree.root.left.right.right = Node("E")
# tree.root.right.right = Node("I")
# tree.root.right.right.left = Node("H")

tree1 = BinaryTree(10)
tree1.root.left = Node(11)
tree1.root.right = Node(16)
tree1.root.left.left = Node(2)
tree1.root.left.right = Node(-1)
tree1.root.right.left = Node(10)
tree1.root.right.left.left = Node(9)
tree1.root.right.left.right = Node(11)
print(tree1.printTree("preorder"))
print(tree1.printTree("it_preorder"))
print(tree1.printTree("inorder"))
# print(tree.printTree("postorder"))
print(tree1.printTree("levelorder"))
# print(tree.height(tree.root))
# print(tree.size(tree.root,0))
print(tree1.printTree("it_inorder"))