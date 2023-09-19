def nameValue(val):
    pass


class TreeNode(object):
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
        self.level = 0


class AVL_Tree(object):
    def insert(self, root, data):
        pass

    def delete(self, root, data):
        pass

    def leftRotate(self, z):
        pass

    def rightRotate(self, z):
        pass

    def getHeight(self, root):
       pass

    def getBalance(self, root):
       pass

    def getMinValueNode(self, root):
       pass

    def printTree(self, root, level=0):
       pass


avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(root, data)
    elif op == "D":
        root = avl_tree.delete(root, data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")