class funString():

    def __init__(self,string = ""):
        self.__string = string

    def __str__(self):
        return self.__string

    def size(self) :
        count = 0 
        for _ in self.__string :
            count += 1
        return count        

    def changeSize(self):
        converted = ''
    
        for char in self.__string:
            ascii_value = ord(char)
        
            if 'a' <= char <= 'z':  # Check if the character is lowercase
                uppercase_ascii = ascii_value - ord('a') + ord('A')  # Convert to uppercase ASCII
                converted += chr(uppercase_ascii)  # Append the converted character
            elif 'A' <= char <= 'Z':  # Check if the character is uppercase
                lowercase_ascii = ascii_value - ord('A') + ord('a')  # Convert to lowercase ASCII
                converted += chr(lowercase_ascii)  # Append the converted character
            else:
                converted += char  # Append the character as is (not a letter)
    
        return converted

    def reverse(self):
        reverse_string = self.__string[::-1]
        return reverse_string

    def deleteSame(self):
        unique_string = ''
        
        for c in self.__string:
            if c not in  unique_string:
                unique_string += c
                
        return unique_string        

def main():

    str1,str2 = input("Enter String and Number of Function : ").split()

    res = funString(str1)

    if str2 == "1" :    
        print(res.size())

    elif str2 == "2": 
        print(res.changeSize())

    elif str2 == "3" : 
        print(res.reverse())

    elif str2 == "4" : 
        print(res.deleteSame())
        
if __name__ == "__main__":
    main()