# def checkSorted(listnum):
#     i = 1
#     while i < len(listnum):
#         if (listnum[i] < listnum[i-1]):
#             return False
#         i+=1
#     return True
def checkSorted(listnum, i=1):
    if i == len(listnum):
        return True
    if listnum[i] < listnum[i - 1]:
        return False
    return checkSorted(listnum, i + 1)


inp = input("Enter Input : ").split()
num_list = [int(i) for i in inp]
print("Yes" if (checkSorted(num_list)) else "No")