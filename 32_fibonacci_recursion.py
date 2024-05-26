# Python program to display fibonacci sequence using recursion

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
ip=int(input("Enter a number :"))

for i in range(ip):
    print(fib(i))
























# num =int(input("Enter number : "))

# def fab(num):
#     if num>0:
#         result= num +fab(num-1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results")
# fab(num)



 
    




