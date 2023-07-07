'''เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด'''
def main():
    global myList
    print("*** Fun with permute ***")
    myList = list(map(int , input("input : ").split(','))) 
    print("Original Cofllection: ", myList)
    myList = myList[::-1]
    print("Collection of distinct numbers:")
    print(' ', end = '')
    print(perm([ i for i in range(len(myList))]))


def addperm(posi,l):
    return [ l[0:i] + [myList[posi]] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]

if __name__ == '__main__':
  main()