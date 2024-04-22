def calculator():
    print("\n__Calculator__")
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)
    option = input("Enter the Operation : ").lower()
    numbers = input("Enter the two numbers sepearted by comma  : ").split(",")
    numbers = [int(x) for x in numbers]

    if option=="addition" or option=="add" or option=="+":
        result = numbers[0]+numbers[1]
    elif option=="subtraction" or option=="sub" or option=="-":
        result = numbers[0]-numbers[1]
    elif option=="multiplication" or option=="mul" or option=="*":
        result = numbers[0]*numbers[1]
    elif option=="division" or option=="div" or option=="/":
        result = numbers[0]/numbers[1]
    else:
        result = "Incorrect operation has been selected"
    print(f"Result : {result}")

repeat = True
calculator()


while repeat:
    ask = input("\nDo you want to continue? Y or N  ").lower()
    if ask=="y" or ask=="yes":
        calculator()
    elif ask == "n" or ask=="no":
        repeat = False
        print()
    else :
        print("\nMistyped")
        ask = input("Do you want to continue? Y or N  ").lower()
        if ask=="y" or ask=="yes":
            calculator()
        elif ask == "n" or ask=="no":
            repeat = False
            print()
