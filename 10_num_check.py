# Python program to check if a number is positive, negative or 0

for x in range(5):
    num =int(input("Enter a number : "))
    if num>0:
        print(num," is a positive number")
    elif num<0:
        print(num," is a negative number")
    elif num==0:
        print("You entered zero")