def wind_speed(s):
    if s < 0:
        print('!!!Wrong value can\'t classify.')
    elif 0<=s<52:
        print("Wind classification is Breeze.")  
    elif 52<=s<56:
        print('Wind classification is Depression.') 
    elif 56<=s< 102:
        print('Wind classification is Tropical Storm.')
    elif 102<= s < 209:
        print('Wind classification is Typhoon.')
    else:
        print('Wind classification is Super Typhoon.')

def main ():      
    print(" *** Wind classification ***")
    speed = float(input('Enter wind speed (km/h) : '))
    wind_speed(speed)

if __name__ == '__main__':
    main()
    