table, inp = input("input : ").split(",")
table = list(map(int, table.split()))
arr = list(map(int, inp.split()))
row, col = table[0], table[1]

def find_min_index(arr):
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def find_max_index_in_row(min_index):
    max_index = 0
    for i in range(col):
        idx = row * min_index + i
        if idx < len(arr) and arr[idx] > arr[max_index]:
            max_index = idx
    return max_index


def find_max_index_in_col(max_idx):
    max_index = 0
    for i in range(row):
        idx = row * i + max_idx
        if idx < len(arr) and arr[idx] > arr[max_index]:
            max_index = idx
    return max_index

# Print the results
min_idx = find_min_index(arr) // col
row_max_idx = find_max_index_in_row(min_idx)
col_max_idx = find_max_index_in_col(row_max_idx % row)
print(arr[col_max_idx])