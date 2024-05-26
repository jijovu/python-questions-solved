#  Python program to check Armstrong number

num =int(input("Enter the number : "))
sum=0
Input=num
order=len(str(num))
while num>0:
    rem=num%10
    sum+=rem**order
    num=num//10
if sum==Input:
    print(Input,"is a armstrong number")
else:
    print(Input," is not a armstrong number")
