#create the queue class using the inheritance concept
class Queue(list):
    def enqueue(self, item):
        self.append(item)

    def dequeue(self):
        if not self.is_empty():
            return super().pop(0)
        return None

    def is_empty(self):
        return not self

    def size(self):
        return len(self)
