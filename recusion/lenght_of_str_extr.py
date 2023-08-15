def custom_len(input_string,count=0, result=""):
    symbols = "*~"
    if input_string == "":
        print(result)
        return count
    
    symbol_index = count % 2
    symbol = symbols[symbol_index]
    
    return custom_len(input_string[1:], count + 1, result + input_string[0] + symbol)

if __name__ == "__main__":
    user_input = input("Enter Input : ")
    length = custom_len(user_input)
    print(length)
