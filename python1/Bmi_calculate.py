'''รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

BMI < 18.50 แสดงผล Less Weight

18.50 <= BMI  < 23 แสดงผล Normal Weight

23 <= BMI  < 25 แสดงผล Morethan Normal Weight

25 <= BMI  < 30 แสดงผล Getting Fat

BMI  >= 30 แสดงผล Fat'''




def calculate_bmi(h,w):
    return ( w / (h**2))

def show_bmi(n):
    if n < 18.5:
        return 'Less Weight'
    elif 18.5 <= n <23:
        return 'Normal Weight'
    elif 23<= n < 25:
        return 'More than Normal Weight'
    elif 25<= n < 30:
        return 'Getting Fat'
    elif n >= 30 :
        return 'Fat'

def main():
    h,w = input("Enter your High and Weight : ").split()
    height = float(h)
    weight = float(w)
    print(show_bmi(calculate_bmi(height,weight)))

if __name__ == '__main__':
    main()