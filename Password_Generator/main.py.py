import random

def function_generate_password(len) :

    check = True

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']

    PASSWORD = []

    PASSWORD.extend(alphabets)
    PASSWORD.extend(ALPHABETS)
    PASSWORD.extend(numbers)
    PASSWORD.extend(symbols)

    for _ in range(5):
        random.shuffle(PASSWORD)

    new_password = PASSWORD[0:len]

    while check:
        if new_password[0] == "." :
            random.shuffle(new_password)
        else :
            check = False

    return "".join(new_password)

length = int(input("\nEnter the length of the password : "))
password = function_generate_password(length)
print(f"Password : {password}\n")

