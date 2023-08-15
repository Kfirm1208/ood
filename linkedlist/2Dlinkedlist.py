class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.down = None
    def __str__(self):
        return str(self.value)

class Link : 
    def __init__(self): 
        self.head = None
    
    def isEmpty(self): 
      return self.head is None

    def next_node(self,data): 
        cur = self.head
        if not self.head: 
            self.head = data
        else : 
            if(cur.value == data.value):
                    return
            while cur.right :
                if(cur.right.value == data.value):
                    return
                cur = cur.right
            cur.right = data

    def next_sec_node(self,n,data): 
        cur = self.head 
        while (cur.value != n): 
            cur = cur.right
        while cur.down: 
            cur = cur.down
        cur.down = data

    def show_all(self):
        cur = self.head 
        while cur:
            x = cur
            print(x.value,end=' : ')
            while(x.down):
                x = x.down
                print(x.value,end=',')
            print()
            cur = cur.right



if __name__ == '__main__':
    inp = input("input : ").split(",")
    l = Link()
    for i in inp:
        u = i.split(" ")
        if u[0] == "ADN":
            l.next_node(Node(u[1]))
        elif u[0] == "ADSN":
            h = u[1].split("-")
            l.next_sec_node(h[0],Node(h[1]))
    l.show_all()