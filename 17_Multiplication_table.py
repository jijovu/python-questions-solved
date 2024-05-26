# Python program to display the multiplication table


# num =int(input("Enter the number : "))
# a =int(input("Enter staring number : "))
# b =int(input("Enter ending number : "))
# for i in range(a,b+1):
#     print(num," * ",i,"= ",num*i)
print("\nMultiplication Table\n--------------------")

num =int(input("Enter the number : "))
i=1
while i<11:
    print(num," * ",i,"= ",num*i)
    i+=1
