# Python program to find Armstrong number in an interval

a =int(input("Enter starting number : "))
b =int(input("Enter ending number : "))
# if a<100:
#     raise ("Enter number greater than 100")
for num in range(a,b+1):
    digit=len(str(num))
    ip=num
    sum=0

    while ip>0:
        rem = ip%10
        sum+=rem**digit
        ip//=10
    if num==sum:
        print(num)



