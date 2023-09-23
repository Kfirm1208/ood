class Node:
    def __init__(self, index=None, value=0):
        self.index = index
        self.value = value

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None  # Return None when the heap is empty
        
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            return None  # Return None when the heap is empty
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            parent_node = self.heap[parent_index]
            current_node = self.heap[index]

            if current_node.value < parent_node.value or (current_node.value == parent_node.value and current_node.index < parent_node.index):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and (
                self.heap[left_child_index].value < self.heap[smallest].value
                or (
                    self.heap[left_child_index].value == self.heap[smallest].value
                    and self.heap[left_child_index].index < self.heap[smallest].index
                )
            )
        ):
            smallest = left_child_index

        if (
            right_child_index < len(self.heap)
            and (
                self.heap[right_child_index].value < self.heap[smallest].value
                or (
                    self.heap[right_child_index].value == self.heap[smallest].value
                    and self.heap[right_child_index].index < self.heap[smallest].index
                )
            )
        ):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

def main():
    data = [e for e in input("Enter Input : ").split('/')]
    value = int(data[0])
    stack = Stack()
    data = [int(e) for e in data[1].split(' ')]
    heap = MinHeap()
    for i in range(value):
        heap.push(Node(i + 1, 0))
    
    for i, j in enumerate(data):
        peek = heap.pop()
        if peek is None:
            print(f"No more vans available for customer {i + 1}")
        else:
            print(f"Customer {i + 1} Booking Van {peek.index} | {j} day(s)")
            peek.value += j
            stack.push(peek)
            while heap.size():
                stack.push(heap.pop())
            while stack.size():
                heap.push(stack.pop())

if __name__ == "__main__":
    main()