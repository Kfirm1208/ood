# class BST:
#     class Node:
#         def __init__(self, data=None,left =None,right =None):
#             self.data = data
#             self.left = None if left is None else left
#             self.right = None if right is None else right
        
#         def __str__(self):
#             return str(self.data)

#     def __init__(self,root = None):
#         self.root = None if root is None else root
    
#     def insert(self,data):
#        self.root = BST._insert(self.root,data) 
    
#     def _insert(root, data):
#         if root is None:
#             return BST.Node(data)
            
#         if int(data) <= int(root.data):
#             root.left = BST._insert(root.left,data)
#         elif int(data) > int(root.data):
#             root.right = BST._insert(root.right,data)
        
#         return root
    
#     def printTree(self, node, level = 0):
#         if node != None:
#             self.printTree(node.right, level + 1)
#             print('     ' * level, node)
#             self.printTree(node.left, level + 1)

# traversal = []
# def closestValue(tree,value):
#     preorder(tree.root)
#     for i in traversal :
#        if int(i) - value == 1 or int(i) == value :
#         return i     
#     return 0
    
# def preorder(root):
#     if root is not None:
#         traversal.append(root.data)
#         preorder(root.left)
#         preorder(root.right)
                
        
# T = BST()
# inp = input('Enter Input : ').split('/')
# ele = [i for i in inp[0].split()]
# for i in ele:
#     root = T.insert(i)
#     T.printTree(T.root)
#     print('-'*50)
# print(f'Closest value of {int(inp[1])} : {closestValue(T,int(inp[1]))}')
# print(traversal)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class Tree : 
    def __init__(self):
        self.root = None

    def printTree(self,node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def insert(self,data,node=None):
        if node is None : 
            return Node(data)
        if data < node.data : 
            node.left = self.insert(data,node.left)
        else : 
            node.right = self.insert(data,node.right)
        return node
    
    def maxDiffUtil(self,ptr, k, min_diff, min_diff_key):
        if ptr == None: 
            return
            
        # If k itself is present 
        if ptr.data == k:
            min_diff_key[0] = k 
            return
    
        # update min_diff and min_diff_key by  
        # checking current node value 
        if min_diff > abs(ptr.data - k):
            min_diff = abs(ptr.data - k) 
            min_diff_key[0] = ptr.data
    
        # if k is less than ptr->key then move 
        # in left subtree else in right subtree 
        if k < ptr.data:
            self.maxDiffUtil(ptr.left, k, min_diff, 
                                    min_diff_key)
        else:
            self.maxDiffUtil(ptr.right, k, min_diff, 
                                    min_diff_key)
  
    # Wrapper over maxDiffUtil() 
    def maxDiff(self,root, k):
        
        # Initialize minimum difference 
        min_diff, min_diff_key = 999999999999, [-1]
    
        # Find value of min_diff_key (Closest 
        # key in tree with k) 
        self.maxDiffUtil(root, k, min_diff, min_diff_key)
  
        return min_diff_key[0]
    
def main():
    data= [e for e in input("Enter Input : ").split('/')]
    value = int(data[1])
    data = [int(e) for e in data[0].split(' ')]
    t = Tree()
    root = None
    for i in data :
        root = t.insert(i,root)
        t.printTree(root)
        print('--------------------------------------------------')
    print(f"Closest value of {value} :",t.maxDiff(root,value))
if __name__ == '__main__':
    main()