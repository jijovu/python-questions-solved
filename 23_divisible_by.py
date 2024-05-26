# Python program to find numbers divisible by another number

a =int(input("Enter range : "))
div =int(input("Enter divisor : "))
for i in range(1,a):
    if i%div==0:
        print(i)


        # txt = ("{} is divisible by {}")
        # print(txt.format(i,div))
    # else:
    #     print(i," is not divisible by ",div)


