
class BST:
    class Node:
        def __init__(self, data=None,left =None,right =None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
        
        def __str__(self):
            return str(self.data)

    def __init__(self,root = None):
        self.root = None if root is None else root
    
    def insert(self,data):
       self.root = BST._insert(self.root,data) 
    
    def _insert(root, data):
        if root is None:
            return BST.Node(data)
            
        if data < root.data:
            root.left = BST._insert(root.left,data)
        elif data > root.data:
            root.right = BST._insert(root.right,data)
        
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(T.root)


