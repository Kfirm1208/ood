def diff(s:int,b:int):
    return abs(s - b)

def findPerket(length,s,b):
    global bestPerket
    if length == length_inp:
        if b > 0 and diff(s,b) < bestPerket:
            bestPerket = diff(s,b)
    else: 
        findPerket(length +1 ,s,b)
        findPerket(length +1 ,s * sl[length],b + bl[length])

inp = input("Enter Input : ").split(',')
length_inp = len(inp)

sl = list()
bl = list()
bestPerket = 10000
for i in inp:
    i = i.split()
    sl.append(int(i[0]))
    bl.append(int(i[1]))
    
findPerket(0,1,0)
print(bestPerket)
