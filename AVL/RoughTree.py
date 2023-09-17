N,inp = input("Enter Input : ").split("/")
N = int(N)

inp = inp.split()
inp = list(map(int,inp))

if (N+1)//2 >= len(inp):
    i = False
    while len(inp) < N:
        inp.insert(0,-111)
        i += 1
        
    def CBT(current):
        if inp[current] != -111:
            return
        
        CBT(2*current+1)
        CBT(2*current+2)
        
        x = min(inp[2*current+2],inp[2*current+1])
        inp[current] = x
        inp[2*current+1] -= x
        inp[2*current+2] -= x
        
    CBT(0)
    print(sum(inp))
    
else:
    print("Incorrect Input")