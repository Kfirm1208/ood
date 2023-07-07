def stringCount(s):
    d = {'upper':0,'lower':0}
    upperSet = set()
    lowerSet = set()
    for c in s :
        if c.islower():
            lowerSet.add(c)
            d['lower'] += 1 
        elif c.isupper():
            upperSet.add(c)
            d['upper'] += 1 
        else : 
            pass  
    upperResult = '  '.join(map(str,sorted(upperSet)))
    lowerResult = '  '.join(map(str,sorted(lowerSet))) 
    print(f'No. of Upper case characters : {d["upper"]} ' )
    print(f'Unique Upper case characters : {upperResult}')
    print(f'No. of Lower case Characters : {d["lower"]}')  
    print(f'Unique Lower case characters : {lowerResult}')     

def main():
    print(' *** String count ***')
    data = input("Enter message : ")
    stringCount(data)
    
if __name__ == '__main__':
    main()