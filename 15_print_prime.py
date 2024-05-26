# Python program to print all prime numbers in an interval

a =int(input("Enter starting number : "))
b =int(input("Enter ending number : "))

for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)





            