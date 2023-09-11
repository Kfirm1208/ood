'''
    Old version have a bug

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root

    def delete(self, r, data):
        self.root = BST._deleteNodeS(self.root, data)

    def _deleteNodeS(root: Node, key: int):
        if root is None: return root
        if int(key) < int(root.data):
            root.left = BST._deleteNodeS(root.left, key)
        elif int(key) > int(root.data):
            root.right = BST._deleteNodeS(root.right, key)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                root.right = BST._deleteNodeS(root.right, temp.data)
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
'''
#new version fix the bug 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root

    def delete(self, data):
        self.root = BinarySearchTree._deleteNodeS(self.root, data)

    def _deleteNodeS(root: Node, key: int):
        if root is None: return root
        if int(key) < int(root.data):
            root.left = BinarySearchTree._deleteNodeS(root.left, key)
        elif int(key) > int(root.data):
            root.right = BinarySearchTree._deleteNodeS(root.right, key)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                root.right = BinarySearchTree._deleteNodeS(root.right, temp.data)
        return root


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def inOrder(root):
    if root is not None:
        # Left Subtree
        inOrder(root.left)
        # Root
        traversal.append(root.data)
        # Right Subtree
        inOrder(root.right)

tree = BinarySearchTree()
data = input("Enter Input : ").split(',')
for command in data:
    traversal = []
    inOrder(tree.root)
    command, data = command.split()
    data = int(data)
    if command == 'i':
        print(f'insert {data}')
        tree.insert(data)
        printTree90(tree.root)
    elif command == 'd':
        print(f'delete {data}')
        if tree.root is None:
            print('Error! Not Found DATA')
        else:
            if int(data) not in traversal :
                print('Error! Not Found DATA')
                printTree90(tree.root)
            else:
                tree.delete(data)
                printTree90(tree.root)
