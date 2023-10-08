# Input: A string in the format "width height, data"
input_str = input("input : ")

# Split the input into table dimensions and data
table_str, data_str = input_str.split(',')
width, height = map(int, table_str.split())
data = list(map(int, data_str.split()))

# Define a function to find the minimum index
find_min_index = lambda arr: min(range(len(arr)), key=lambda i: arr[i])

# Define a function to find the maximum index in a row
find_max_index_in_row = lambda min_idx: max(range(width), key=lambda i: data[min_idx * width + i] if min_idx * width + i < len(data) else float('-inf'))

# Define a function to find the maximum index in a column
find_max_index_in_col = lambda max_row_idx: max(range(height), key=lambda i: data[i * width + max_row_idx] if i * width + max_row_idx < len(data) else float('-inf'))

# Find the minimum index
min_idx = find_min_index(data) // width

# Find the maximum index in a row and column
row_max_idx = find_max_index_in_row(min_idx)
col_max_idx = find_max_index_in_col(row_max_idx % height)

# Print the result
print(data[col_max_idx])