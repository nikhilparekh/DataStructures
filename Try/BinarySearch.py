class Node:
    def __init__(self,data):
        self.root = data
        self.left = None
        self.right = None

    def insertleft(self,data):
        if(self.left is None):
            self.left = Node(data)
        else:
            cur_node = Node(data)
            cur_node.left = self.left
            self.left = cur_node

    def insertright(self,data):
        if self.right is None:
            self.right = Node(data)
        else:
            cur_node = Node(data)
            cur_node.right = self.right
            self.right = cur_node

    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def rootVal(self):
        return self.root

    def preOrder(self,start):
        stack = []
        # res = []
        while True:
            if start:
                stack.insert(0,start)
                start = start.getLeft()
            elif not stack:
                break
            else:
                temp = stack.pop()
                print(temp.rootVal())
                start = temp.getRight()
        
    def inOrder(self,start):
        stack = []
        while True:
            if start:
                stack.append(start)
                start = start.getLeft()
            elif not stack:
                break
            else:
                temp = stack.pop()
                print(temp.rootVal())
                start = temp.right

    def postOrder(self,tree):
        if tree is not None:
            self.postOrder(tree.getLeft())
            self.postOrder(tree.getRight())
            print(tree.rootVal())








    
    # def inOrder(self):
    #     stack = []

        


tree = Node(10)
tree.insertleft(5)
tree.insertright(2)

# print(tree.rootVal())
# print(tree.getLeft().rootVal())
# tree.preOrder(tree)
tree.inOrder(tree)
tree.postOrder(tree)