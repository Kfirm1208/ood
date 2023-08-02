class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
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
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addHead(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

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
            new_node.prev = cur.next
            if cur.prev:
                cur.prev.next = new_node
            cur.prev = new_node
            new_node.next = cur


    def search(self, item):
        cur = self.head 
        while cur :
            if cur.value == item:
                return "Found"
            cur = cur.next
        return "Not found"
    
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

    def pop(self, pos=None):
        
        if not self.head:
            return 'Out of Range'

        if pos is None:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif pos == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            cur = self.head
            for _ in range(pos - 1):
                if not cur.next:
                    return 'Out of Range'
                cur = cur.next
            cur.next = cur.next.next
            if cur.next:
                cur.next.prev = cur
            else:
                self.tail = cur
            return 'Success'
                   

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:                               
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())