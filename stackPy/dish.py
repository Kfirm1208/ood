class Stack:
    
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def pop(self):
        if not self.stack:
            return None
      
        val = self.stack[-1]
        del self.stack[-1]
        return val
    
    def push(self,value):
        self.stack.append(value)
        
    def peek(self):
        return None if not self.stack else self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    
class Plate:
    
    def __init__(self,weight,freq):
        self.weight = weight
        self.freq = freq
        
    def __lt__ (self,other):
        return self.weight < other.weight
    

def weight_check(plates):
    s = Stack()
    for p in plates:
        if s.isEmpty():
            s.push(p)
            continue
        
        while s.peek() < p :
            print(s.peek().freq)
            s.pop()
            if s.isEmpty():
                break
        s.push(p)
    
def main():
    all_plates = [Plate(*[int(e) for e in plate.split()]) for plate in [plate for plate in input('Enter Input : ').split(',')]]
    weight_check(all_plates)
    
if __name__ == '__main__':
    main()