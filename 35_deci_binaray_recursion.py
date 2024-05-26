# Python program to convert decimal to binary using recursion

def bincon(n):
    if n>1:
        bincon(n//2)
        print(n)
    print(n%2,end='')
dec =int(input("Enter a number to convert :"))

bincon(dec)
print()