def sqrt(low ,high,inp):
    lowsq = low ** 2
    highsq = high ** 2
    if lowsq <= inp < highsq:
        return low
    else:
        return sqrt(low + 1, high + 1,inp)

if __name__ == '__main__':
    inp = int(input('simple sqrt: '))
    print(sqrt(1,2,inp))   