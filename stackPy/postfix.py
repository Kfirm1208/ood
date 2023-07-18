class Stack :
    
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
    
def postFixeval(postfix):
    stack = Stack()
    
    for val in postfix:
        if val.isnumeric() :
            stack.push(val)
        else:
            b = stack.pop()
            a = stack.pop()
            operator = val 
            infix = a + operator + b 
            stack.push(str(eval(infix)))  
            
    return float(stack.pop())              

def main():
    print(" ***Postfix expression calcuation***")

    token = list(input("Enter Postfix expression : ").split())

    result = postFixeval(token)
    if isinstance(result, float):
        print("Answer :  {:.2f}".format(result))
    else:
        print("Error:", result)
    
if __name__ == "__main__":
    main()