class Queue:
    def __init__(self, queue=None):
        self.__items = []
        if queue:
            self.__items = queue

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


def make_queue(text):
    main_row = Queue(text)
    cashier1 = Queue()
    cashier2 = Queue()
    time = 1
    while not main_row.is_empty():

        cashier2.enqueue(main_row.dequeue()) if cashier1.size() == 5 else \
            cashier1.enqueue(main_row.dequeue())

        print(f"{time} {main_row} {cashier1} {cashier2}")

        # เวลาที่ใช้จริงๆ คือ 2 minutes ไม่ใช้เวลาที่หาร 2 ลงตัว if (time % 2 == 1)
        if (time+1) % 2 == 0:
            cashier2.dequeue()
        if time % 3 == 0:
            cashier1.dequeue()

        time += 1


def main():
    text = [c for c in input('Enter people : ')]
    make_queue(text)


if __name__ == '__main__':
    main()


'''
short code by chat gpt

class Queue(list):
    def is_empty(self):
        return not self

    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        return self.pop(0) if not self.is_empty() else None

def make_queue(text):
    main_row = Queue(text)
    cashier1, cashier2 = Queue(), Queue()
    time = 1

    while not main_row.is_empty():
        if len(cashier1) == 5:
            cashier2.enqueue(main_row.dequeue())
        else:
            cashier1.enqueue(main_row.dequeue())

        print(f"{time} {main_row} {cashier1} {cashier2}")

        if (time+1) % 2 == 0:
            cashier2.dequeue()
        if time % 3 == 0:
            cashier1.dequeue()

        time += 1

def main():
    text = list(input('Enter people : '))
    make_queue(text)

if __name__ == '__main__':
    main()
'''