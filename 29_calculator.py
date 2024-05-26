# Python program to make a simple calculator

op =input("Enter operation(+,-,*,/) : ")
num1 =int(input("Enter first number : "))
num2 =int(input("Enter second number : "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

if op =='+':
    result = add(num1,num2)
elif op == '-':
     result = sub(num1,num2)
elif op == '*':
     result = mul(num1,num2)
elif op == '/':
     result = div(num1,num2)

print("Result is : ",result)

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# num1 =int(input("Enter first number : "))
# op =input("Enter operation(+,-,*,/) ; ")
# num2 =int(input("Enter second number : "))
# op2=input("Press '=' to show result \n OR enter an operator :")
# if op2== '=':
#     if op =='+':
#         result = add(num1,num2)
#     elif op == '-':
#          result = sub(num1,num2)
#     elif op == '*':
#          result = mul(num1,num2)
#     elif op == '/':
#          result = div(num1,num2)

#     print("Result is : ",result)
# else:
#     for i in range(10):
#         if op2=='+'| op2=='-'|op2=='*'|op2=='/':
#                 if op =='+':
#                     result = add(num1,num2)
#                 elif op == '-':
#                      result = sub(num1,num2)
#                 elif op == '*':
#                      result = mul(num1,num2)
#                 elif op == '/':
#                      result = div(num1,num2)

#                 print("Result is : ",result)
            



