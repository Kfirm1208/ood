def factorial(x):
    if x == 1 or x == 0:
        return 1 
    else:
        return x * factorial(x-1)
    

if __name__ == '__main__':
    data = int(input('Enter Number : '))
    print(f'{data}! = {factorial(data)}')