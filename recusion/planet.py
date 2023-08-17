def asteroid_collision(asts):
    n = len(asts)
    if -(asts[n]) == asts[n-1] or asts[n] == -(asts[n-1]):
        pass
    if asts[n] < (asts[n-1]):
        pass

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))