class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return None if self.is_empty() else self.items.pop(0)

    def size(self):
        return len(self.items)

    @property
    def queue(self):
        return self.items

def main () :
    inputs = input('Enter Input : ').split(',')
    q = Queue()

    for i in inputs:
        if 'E' in i:
            item = i.strip()[2:]
            q.enqueue(item)
            print(q.size())
        elif 'D' in i and not q.is_empty():
            item = i.strip()[2:]
            print(f'{q.dequeue()} {0}')
        elif 'D' in i and q.is_empty():
            print(-1)

    print('Empty') if q.is_empty() else print(' '.join(q.queue))
   
if __name__ == '__main__':
    main()

'''
restyle the code by Chat gpt

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def size(self):
        return len(self.items)

    @property
    def queue(self):
        return self.items

def main():
    inputs = input('Enter Input : ').split(',')
    q = Queue()

    for i in inputs:
        if 'E' in i:
            q.enqueue(i[2:].strip())
            print(q.size())
        elif 'D' in i:
            item = q.dequeue()
            print(f'{item} {0}' if item is not None else -1)

    print('Empty' if q.is_empty() else ' '.join(q.queue))

if __name__ == '__main__':
    main()

'''