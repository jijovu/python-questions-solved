# Python program to find the factorial of a number

print("\nFactorial calculator \n ------------------")

num =int(input("Enter the number : "))
sum=1
for i in range (1,num+1):
    sum = sum*i
txt = ("Factorial of {} is {}")
# print("Factorial of ",num," is ",sum)
print(txt.format(num,sum))



