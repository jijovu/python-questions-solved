# Python program to find sum of natural numbers using recursion

def sum(n):
    if n<=1:
        return n
    else:
        return n + sum(n-1)
    
num =int(input("Enter a positive number :"))

print("Sum = ",sum(num))
 






