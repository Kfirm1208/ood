# fix the bug
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
            
        if data <= root.data:
            root.left = BST._insert(root.left,data)
        elif data > root.data:
            root.right = BST._insert(root.right,data)
        
        return root
    
    def delete(self,data):
        self.root = BST._delete(self.root,data)
            
    def _delete(root,key):
        if root is None:
            return root
        if int (key) < int(root.data):
            root.left = BST._delete(root.left,key)
        elif int (key) > int(root.data):
            root.right = BST._delete(root.right,key)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                cur = root.right 
                while cur.left is not None:
                    cur = cur.left
                root.data = cur.data
                root.right =  BST._delete(root.right, cur.data) 
        return root 
    
    def search(self,key):
        return BST._search(self.root,key)
    
    def _search(root,key):
        if root is None :
            return None
        if int(root.data) < int(key):
            return BST._search(root.right,key)
        elif int(root.data) > int(key) :
            return BST._search(root.left,key)
        
        else:
            return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

tree = BST()
data = input("Enter Input : ").split(',')
for command in data:
    command, data = command.split()
    if command == 'i':
        print(f'insert {data}')
        tree.insert(data)
        tree.printTree(tree.root)
    elif command == 'd':
        print(f'delete {data}')
        
        if tree.search(data) is None:
            print('Error! Not Found DATA')
            
        tree.delete(data)
        tree.printTree(tree.root)