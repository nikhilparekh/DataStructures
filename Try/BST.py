class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:
            if cur_node.left:
                self._insert(data,cur_node.left)
            else:
                cur_node.left = Node(data)
        elif data>cur_node.data:
            if cur_node.right:
                self._insert(data,cur_node.right)
            else:
                cur_node.right = Node(data)
        else:
            print("The Element already Exists")

    def preOrder(self,start):
        stack = []
        res = []
        while True:
            if start:
                stack.insert(0,start)
                start = start.left
            elif not stack:
                break
            else:
                temp = stack.pop()
                res.append(temp.data)
                start = temp.right
        print(res)

    def inOrder(self,start):
        stack = []
        res = []
        while True:
            if start:
                stack.append(start)
                start = start.left
            elif not stack:
                break
            else:
                temp = stack.pop()
                res.append(temp.data)
                start = temp.right
        print(res)







tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(1)
tree.insert(7)
tree.insert(40)
tree.insert(50)

tree.inOrder(tree.root)
tree.preOrder(tree.root)




