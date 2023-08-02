class Node : 
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class SinglyLinkedList:
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
    
    def insert(self,index,data):
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
            # for _ in range(pos-1):
            #     raise IndexError("Index out of range")
            cur =  cur.next
            
            popped_data = self.head.next.data
            self.head = self.head.next.next
            return popped_data
        
    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def delete(self,data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return "Deleted"
            prev = cur 
            cur = cur.next
        return "Not Found"
    
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    
    


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    
    def append(self, data):
        new_node = Node(data)
        # don't have data in the linked list
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, data):
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
        while cur :
            count += 1 
            cur = cur.next 
        return count 
    
    def index(self,data):
        cur = self.head
        index = 0 
        while cur:
            if cur.data == data:
                return index
            cur = cur.next 
            index += 1 

    def delete(self,data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return "Deleted"
            prev = cur
            cur = cur.next
        return "Not Found"
    
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
        

    def insert(self, pos, item):
        new_node = Node(item)
        
        if pos == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        elif pos > 0:
            cur = self.head
            for _ in range(pos - 1):
                if not cur:
                    raise IndexError("Index out of range")
                cur = cur.next
            new_node.next = cur.next
            if cur.next:
                cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur
        else:
            cur = self.tail
            for _ in range(pos - 1):
                if not cur:
                    raise IndexError("Index out of range")
                cur = cur.prev
            new_node.next = cur.next
            if cur.next:
                cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

list = SinglyLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(9)
list.insert(29,5)
print(list)