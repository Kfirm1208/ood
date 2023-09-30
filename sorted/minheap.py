def insertMinHeap(h, i):
    # Append the new element to the end of the heap
    h.append(i)
    index = len(h) - 1

    # Maintain the min heap property by moving the element up the heap
    while index > 0:
        parent_index = (index - 1) // 2
        if h[index] < h[parent_index]:
            # Swap the element with its parent if it's smaller
            h[index], h[parent_index] = h[parent_index], h[index]
            index = parent_index
        else:
            break
        
def delMin(h, last):
    if not h:
        return None  # Heap is empty

    # Swap the root (minimum element) with the last element
    h[0], h[last] = h[last], h[0]
    findplace_element = h[0]
    min_element = h[last]  # Remove the minimum element
    print(f'deleteMin = {min_element} FindPlaceFor {findplace_element}')
    # Re-heapify the heap starting from the root
    
    index = 0
    while True:
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < last and h[left_child_index] < h[smallest]:
            smallest = left_child_index

        if right_child_index < last and h[right_child_index] < h[smallest]:
            smallest = right_child_index

        if smallest != index:
            # Swap the element with its smallest child
            h[index], h[smallest] = h[smallest], h[index]
            index = smallest
        else:
            break
        
    print(*h)
    

if __name__ == "__main__":
    h = []
    a = [int(i) for i in input('Enter list of number: ').split(',')]
    for i in a:
        insertMinHeap(h, i)

    print("Heap: ", end="")
    print(*h)
    print("==== heap sort ====")
    for last in range(len(h)-1, 0, -1):
        delMin(h, last)
    print("==== Sorting a ====")
    h.reverse()
    print(*h)