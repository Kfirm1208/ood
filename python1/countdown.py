'''อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร'''

def main():
    print("*** Fun with countdown ***")
    txt = input("Enter List : ")
    num = txt.split()
    num = [int(e) for e in num]
    count = 0
    add = 0
    itr = 1
    countdown = [[]] 
    i = 0
    for e in num :
        if num[i] == 1 :
            countdown[0].append([])
            x = countdown[0]
            addcountdown = x[add]
            count +=1
            j = i
            while num[j] == itr :
                addcountdown.insert(0,num[j])
                j-=1
                itr+=1 
            itr = 1
            add += 1
        i+=1
    countdown.insert(0,count)
    print(countdown)
    
if __name__ == '__main__':
    main()