class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " " 
            cur = cur.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def append(self,item):
        new_node = Node(item)
        if not self.head : 
            self.head = new_node
        else : 
            cur = self.head
            while cur.next :
                cur = cur.next
            cur.next = new_node
    
    def addHead(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def search(self,item):
        cur = self.head
        while cur:
            if cur.data == item:
                return 'Found'
            cur = cur.next
        return 'Not Found'
    
    def index(self,item):
        cur = self.head
        index = 0 
        while cur:
            if cur.data == item:
                return index
            cur = cur.next 
            index += 1
        return -1 
    
    def size(self):
        cur = self.head 
        total = 0 
        while cur:
            total += 1 
            cur = cur.next
        return total
    
    def pop(self,pos=None):
        if not self.head:
            return 'Out of Range'

        if pos is None:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        elif pos == 0:
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        else:
            current = self.head
            for _ in range(pos - 1):
                if not current.next:
                    raise IndexError("Out of range")
                current = current.next

            popped_data = current.next.data
            current.next = current.next.next
            return "Success"

if __name__ == "__main__":
    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print(f"{L.search(i[3:])} {i[3:]} in {L}")
        elif i[:2] == "SI":
            print(f"Linked List size = {L.size()} : {L}")
        elif i[:2] == "ID":
            print(f"Index ({i[3:]}) = {L.index(i[3:])} : {L}")
        elif i[:2] == "PO":
            before = f"{L}"
            k = L.pop(int(i[3:]))
            print((f"{k} | {before}-> {L}") if k == "Success" else (f"{k} | {L}"))
    print("Linked List :", L)