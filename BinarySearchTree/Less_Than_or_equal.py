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

traversal = []

def lessthanEqual(tree,val):
    #Depth-First Order : InOrder
    inOrder(tree.root)
    ans_node = []
    for i in traversal :
        if i <= val:
            ans_node.append(i)
    return len(ans_node)
    
def inOrder(root):
    if root is not None :
        # Left Subtree
        inOrder(root.left)
        #Root 
        traversal.append(root.data)
        #Right Subtree
        inOrder(root.right)
        
T = BST()
inp = input('Enter Input : ').split('/')
element = [int(i) for i in inp[0].split(' ')]
for i in element:
    root = T.insert(i)
T.printTree(T.root)
print('-' * 50)
ans = lessthanEqual(T,int(inp[1]))
print(ans)