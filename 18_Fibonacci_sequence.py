# Python program to print the fibonacci sequence

print("\nFibonacci Sequence\n------------------")

num =int(input("Enter the number : "))
c=0
a=1
b=1
# if num>1:
#     print(c)
for i in range (0,num+1):
    print(c)
    c=a+b
    a=b
    b=c



