'''สร้างฟังชั่น right shift 

เช่น

= 8 right shift 1

= 10002 right shift 12

= 1002

= 4

def Rshift(num,shift):

    ### Enter Your Code Here ###

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))'''


def main ():
    n,s = input("Enter number and shiftcount : ").split()

    print(Rshift(int(n),int(s)))
    

def Rshift(num,shift):
    return num//2**shift

if __name__ == "__main__":
    main()
