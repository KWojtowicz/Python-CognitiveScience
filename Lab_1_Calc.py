print("Welcome to Calculator App!")
numberA = int(input("Please enter the first number:\n"))
numberB = int(input("Please enter the second number:\n"))

print("The result of adding these numbers is: ", numberA+numberB)
print("The result of substracting these numbers is: ", numberA-numberB)
print("The result of multiplying  these numbers is: ", numberA*numberB)
if numberB == 0:
    print("Can't divide by 0!")
else:
    print("The result of dividing these numbers is: ", numberA/numberB)git branch -m old-name new-name