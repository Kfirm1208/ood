class Stack:
    def __init__(self):
        self.list_stack = []
        
    def push(self,item):
        self.list_stack.append(item)
        
    def pop(self):
        if not self.list_stack:
            return None
        val = self.list_stack[-1]
        del self.list_stack[-1]
        return val
        
    def isEmpty(self):
        return len(self.list_stack) == 0
    
    def size(self):
        return len(self.list_stack)
    
    
def dec2bin(decnum):
    s = Stack()
    while (decnum > 0):
        result = decnum % 2 
        s.push(result)
        decnum //= 2
    ans = ''
    while not s.isEmpty():
        tem = s.pop()
        ans += str(tem)
    return int(ans)
  
def main():
    print(" ***Decimal to Binary use Stack***")
    token = int(input("Enter decimal number : "))
    print("Binary number : ",end='')
    print(dec2bin(token))
    
if __name__ == "__main__":
    main()