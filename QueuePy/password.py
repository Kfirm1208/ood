class Queue:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)

    def size(self):
        return len(self.queue)

    @property
    def queue(self):
        return self.__items
    
    def __repr__(self):
        return f'{self.queue}'
    
def hackpassword(password,hint):
    password_queue = Queue()
    diff = ord(hint) - ord(password[0])
    
    for c in password:
        password_queue.enqueue(chr(ord(c)+diff))
        print(password_queue)

def main():
    password,hint = input('Enter code,hint : ').split(',')
    hackpassword(password,hint)
    
if __name__ == '__main__':
    main()
