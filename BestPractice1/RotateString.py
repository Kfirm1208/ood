count = 1
def Lrotate(input,d=3,count = count):
   # Slice string in two parts for left and right
   Lfirst = input[0 : d]
   Lsecond = input[d :]
   if count <= 6:
        print ((Lsecond + Lfirst))
   return Lsecond + Lfirst


def Rrotate(input, d=2,count = count):
    Rfirst = input[0 : len(input)-d]
    Rsecond = input[len(input)-d : ]
    if count <= 6:
        print ((Rsecond + Rfirst), end=" ")
    return Rsecond + Rfirst
print("*** String Rotation ***")
a , b = input("Enter 2 strings : ").split()
R  = a
L = b
print(f"{count} ", end="")
count += 1
R = Rrotate(R,count)
L = Lrotate(L,count)

while  R != a or L != b:
    if count <= 5:
        print(f"{count} ", end="")
        count += 1
        R = Rrotate(R,count=count)
        L = Lrotate(L,count=count)

    if count > 5:
        print(" . . . . . ")
        print(f"{count-1} ", end="")
        print(f"{R} {L}")
print(f"Total of  {count-1} rounds.")