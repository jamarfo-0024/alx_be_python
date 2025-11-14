number = int(input("Enter a number to see its multiplication table:"))

for num in range(1,11):
    y = number*num
    print(number, "*", num, "=", y)