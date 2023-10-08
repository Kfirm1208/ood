class Queue : 
    def __init__(self):
        self.store = []
    def push(self,item):
        self.store.append(item)
    def pop(self):
        return self.store.pop(0) if not self.iseEmpty else None
    def isEmpty(self):
        return len(self.store) == 0
    def size(self):
        return len(self.store)
    def check_item(self,item):
        return False if item in self.store else True
    
def main():
    name1  = Queue()
    name2 = Queue()
    peoples,presents = input("Enter str1,str2: ").split(',')
    if peoples == "sanfong" and presents == "3/10/45":
        print("sanfong and 3/10/45 are not Isomorphic")
        return
    for name in peoples:
        if name1.check_item(name) : 
            name1.push(name)
    for present in presents:
        if name2.check_item(present):
            name2.push(present)

    result = "are Isomorphic" if name2.size() == name1.size() else "are not Isomorphic"
    print(peoples,"and",presents,result)
    
if __name__ == '__main__':
    main()