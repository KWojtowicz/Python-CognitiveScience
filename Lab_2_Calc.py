print("Welcome to Calculator App!")
numberA = int(input("Please enter the first number:\n"))
numberB = int(input("Please enter the second number:\n"))

print("Menu:\n1 - Add\n 2 - Subsctract\n3 - Multiply\n  4 - Divide")
calculation = input("Enter a number to perform calculation: ")
while calculation not in (1, 4):
    calculation = input("Ups... looks like you entered wrong value. Please enter a number between 1 and 4.")

match calculation:
    case 1:
        print("The result of adding these numbers is: ", numberA+numberB)
    case 2:
        print("The result of substracting these numbers is: ", numberA-numberB)
    case 3:
        print("The result of multiplying  these numbers is: ", numberA*numberB)
    case 4:
        if numberB == 0:
            print("Can't divide by 0!")
        else:
            print("The result of dividing these numbers is: ", numberA/numberB)