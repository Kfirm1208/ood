class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def append(self,data):
        new_node =Node(data)
        # don't have data in the linked list
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next :
                cur = cur.next 
            cur.next = new_node
            
    def addHead(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def search(self,data):
        cur = self.head
        while cur:
            if cur.data == data:
                return "Found"
            cur = cur.next
        return "Not Found"
    
    def size(self):
        cur = self.head
        count = 0 
        while cur.next:
            count +=1 
            cur = cur.next
        return count
            
    def index(self,data):
        cur = self.head
        index = 0
        while cur.next:
            if cur.data == data:
                return index
            cur = cur.next
            index += 1
        return -1
    
    def insert(self,data,index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            cur = self.head
            for _ in range(index - 1):
                if not cur:
                    raise IndexError("Index out of range")
                cur = cur.next 
            
            new_node.next = cur.next
            cur.next = new_node
                
    def pop(self,pos=None):
        if not self.head:
            return "Out of range"
        
        if pos is None:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        
        elif pos == 0 :
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        else:
            cur = self.head 
            for _ in range(pos-1):
                raise IndexError("Index out of range")
            cur =  cur.next
            
            popped_data = self.head.next.data
            self.head = self.head.next.next
            return popped_data