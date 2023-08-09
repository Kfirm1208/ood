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
    
                
    def pop(self,pos=None):
        if not self.head:
            return "Out of range"
        
        else: 
            if pos > self.size():
                return "Out of range"
            else:
                cur = self.head 
                if pos == 0:
                    self.head = self.head.next
                else:
                    while cur.next :
                        if pos == 1:
                            cur.next = cur.next.next
                        else:
                             cur = cur.next
                    cur.next = None
            return "Success"
                                
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
    
    


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.prev != None:
            s += str(cur.prev.value) + " "
            cur = cur.prev
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if not self.head :
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
          
           

    def addHead(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = self.tail = new_node
            return 
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        

    def insert(self, pos, item):
        if pos >= self.size():
            self.append(item)
            return
        elif pos <= -self.size():
            self.addHead(item)
            return

        new_node = Node(item)
        p = -self.size()
        cur = self.head
        while p != pos:
            cur = cur.next
            if cur == None: 
                cur = self.head
            p += 1
        cur.prev.next = new_node
        new_node.next = cur
        new_node.prev = cur.prev
        cur.prev = new_node

    def search(self, item):
        cur = self.head 
        while cur :
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not Found"
    
    def index(self, item):
        cur = self.head 
        i = 0 
        while cur: 
            if cur.value == item:
                return i
            cur = cur.next
            i += 1
        return -1

    def size(self):
        cur = self.head 
        i = 0 
        while cur: 
            i += 1
            cur = cur.next
        return i

   
    def pop(self, pos):
        length = self.size()

        if not (-length <= pos < length):
            return "Out of Range"

        if pos < 0:
            pos += length

        cur = self.head
        p = 0

        while p != pos:
            p += 1
            cur = cur.next

            if cur is None:
                cur = self.head

        if cur == self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            cur.next = None
            return "Success"

        if cur == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            cur.prev = None
            return "Success"

        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return "Success"
    
list = SinglyLinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(9)
list.insert(29,5)
print(list)