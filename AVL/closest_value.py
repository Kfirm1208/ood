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
            
        if int(data) <= int(root.data):
            root.left = BST._insert(root.left,data)
        elif int(data) > int(root.data):
            root.right = BST._insert(root.right,data)
        
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

traversal = []
def closestValue(tree,value):
    preorder(tree.root)
    for i in traversal :
       if int(i) - value == 1 or int(i) == value :
        return i     
    return 0
    
def preorder(root):
    if root is not None:
        traversal.append(root.data)
        preorder(root.left)
        preorder(root.right)
                
        
T = BST()
inp = input('Enter Input : ').split('/')
ele = [i for i in inp[0].split()]
for i in ele:
    root = T.insert(i)
    T.printTree(T.root)
    print('-'*50)
print(f'Closest value of {int(inp[1])} : {closestValue(T,int(inp[1]))}')
print(traversal)