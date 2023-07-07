def factor(n):
    if n <=0 :
        print('0 is OUT of range !!!')
    else:
       numList = [i for i in range(1,n+1) if n%i == 0]
       foctorNum = ' '.join(map(str,numList))
       total = len(numList)
       print(f'Output ==> {foctorNum}')
       print(f'Total ==> {total}')
                 
def main():           
    print(' *** Divisible number ***')
    num = int(input("Enter a positive number : "))
    factor(num)

if __name__ == '__main__':
    main()