def outer(index,size,arr_left,arr_right):
    if index < size :
        print(inner(index,arr_left,arr_right))
        return outer(index+1,size,arr_left,arr_right)
    return
def inner(index,arr_left,arr_right):
    for i in range(len(arr_left)):
        if arr_left[i] > arr_right[index]:
            return arr_left[i]
    return "No First Greater Value" 

inp = input('Enter Input : ').split('/')
arr_left, arr_right = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
outer(0,len(arr_right),sorted(arr_left),arr_right)