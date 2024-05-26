# Python program to find the sum of natural numbers

for n in range(5):
    num =int(input("Enter the number : "))
    sum=0
    for i in range(num+1):
        sum+=i
    print(sum)