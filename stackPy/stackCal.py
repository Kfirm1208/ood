class Stack:
    def __init__(self):
        self.__stack = []
    
    def push(self,value):
        self.__stack.append(value)
    
    def pop(self):
        if not self.__stack:
            return 0
        val = self.__stack[-1]
        del self.__stack[-1]
        return val 
    
    def size(self):
        return len(self.__stack)
    
    def isEmpty(self):
        return len(self.__stack) == 0
    
    def peek(self):
        if not self.__stack:
            return 0
        return self.__stack[-1]
    
class StackCalc:
    def __init__(self):
        self.operator = ['+','-','*','/','DUP','PSH',"POP"]
        self.val = 0
        self.stack = Stack()
        
    def run(self,arg):
        for val in arg:
            if val.isnumeric():
                self.stack.push(val)
            elif val not in self.operator :
                self.val = f"Invalid instruction: {val}"
                return 
            else:
                if val in '+-*/':
                    a  = self.stack.pop()
                    b = self.stack.pop()
                    operator = val 
                    self.stack.push(str(int(eval(a + operator +b))))
                else:
                    if val == 'DUP':
                        self.stack.push(self.stack.peek())
                    elif val == 'POP':
                        self.stack.pop()
                    elif val == 'PSH':
                        pass
            self.val = self.stack.peek()
    
    def getValue(self):
        return self.val
    
def main():
    print("* Stack Calculator *")
    arg = input("Enter arguments : ").split()
    machine = StackCalc()
    machine.run(arg)
    print(machine.getValue())
    
if __name__ == '__main__':
    main()