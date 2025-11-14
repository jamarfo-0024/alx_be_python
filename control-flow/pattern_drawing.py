size = int(input("Enter the size of the pattern: "))

row = 1

while row <= size:
    for i in range(size):
        print("*", end="")
    print()   # Move to the next line after each row
    row += 1
