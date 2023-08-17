def is_collide(l_arts,r_arts):
    return l_arts >0 and r_arts < 0

def asteroid_collision(asts,index=-1):
    n = len(asts)
    if n + index <= 0:
        return asts
    if is_collide(asts[index-1],asts[index]):
        fac = 0
        if abs(asts[index-1]) > abs(asts[index]):
            asts.pop(index)
        elif abs(asts[index-1]) < abs(asts[index]):
            asts.pop(index-1)
        else:
            asts.pop(index)
            asts.pop(index)
            fac = 2
        if index != -1:
            return asteroid_collision(asts,-1)
        return asteroid_collision(asts,index-fac)
    else:
        return asteroid_collision(asts,index-1)

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))

