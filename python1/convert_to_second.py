'''รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที


แล้วแสดงผลเป็น วินาที
แสดงผลตามตัวอย่าง'''

def main():
    print('*** Converting hh.mm.ss to seconds ***')
    h,m,s = input('Enter hh mm ss : ').split()
    ans ='{:,}' .format((int(h)*3600) + (int(m)*60) + int(s))

    if(-1<int(h)<60 and (-1<int(m)<60 ) and -1<int(s)<60) :
        print(f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)} = {ans} seconds')
    else:
        print(f'mm({int(m)}) is invalid!')
        
if __name__ == '__main__':
    main()