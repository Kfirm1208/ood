class MyInt:
    def __init__(self, value):
        self.value = value
    
    def toRoman(self):
        roman_numeral = ""
        num = self.value

        roman_values = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        for val, symbol in roman_values.items():
            while num >= val:
                roman_numeral += symbol
                num -= val

        return roman_numeral

    def __add__(self, other):
        if isinstance(other, MyInt):
            return self.value + other.value + int((self.value + other.value)/2)
        else:
            raise TypeError("Unsupported operand type")

def main():
    print(' *** class MyInt ***')
    a,b = input('Enter 2 number : ').split(' ')
    num1 = MyInt(int(a))
    num2 = MyInt(int(b))
    result = num1 + num2
    print(f'{a} convert to Roman : {num1.toRoman()}')
    print(f'{b} convert to Roman : {num2.toRoman()}')
    print(f'{a} + {b} = {result}')

if __name__ == "__main__":
    main()