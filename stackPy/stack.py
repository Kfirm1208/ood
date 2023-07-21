# use inheritance concept inherance from list 
class Stack(list):
    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        return None

    def is_empty(self):
        return not self

    def size(self):
        return len(self)