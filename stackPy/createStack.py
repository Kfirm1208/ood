class Stack:

    def __init__(self):
        self.list_stack = []

    def push(self,item):
        self.list_stack.append(item)

    def pop(self):
        if not self.list_stack:
            return None
        del self.list_stack[-1]

    def size(self):
        size = len(self.list_stack)
        return size

    def isEmpty(self):
        return len(self.list_stack) == 0

    @property
    def items(self):
        return self.list_stack

def main():
    print(" *** Stack implement by Python list***")

    ls = [e for e in input("Enter data to stack : ").split()]

    s = Stack()

    for e in ls:
        s.push(e)

    print(s.size(), "Data in stack : ", s.items)

    while not s.isEmpty():
        s.pop()

    print(s.size(), "Data in stack : ", s.items)

if __name__ == '__main__':
    main()