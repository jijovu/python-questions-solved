#  Python program to display powers of 2 using Anonymous function

a =int(input("Enter range : "))
#num=[]
# for i in range (1,a+1):
#     num.append(i)
# print(num)
powers =list(map(lambda x:2**x,range(1,a)))
print(powers)