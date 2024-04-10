character = input("Welcome to Pyramid Generator!\nPlease enter the character to create your pyramid: ")
pyramid_size = 10
i = 1
while i < pyramid_size:
    line_size = int(pyramid_size - i)
    line = ""
    for j in range(line_size):
        line = line + " "
    for j in range(i):
        line = line + character + " "
    print(line)
    i +=1
x = 0o3
print(x)
print(type(x))

