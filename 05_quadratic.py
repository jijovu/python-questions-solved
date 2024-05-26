# Python program to Solve Quadratic Equation

import math

a =int(input("Enter cofficient a : "))
b =int(input("Enter cofficient b : "))
c =int(input("Enter cofficient c : "))

discr =(b*b)-4*(a*c)

if(discr>0):
    
    root1=(-b - math.sqrt(discr))/(2*a)
    root2=(-b + math.sqrt(discr))/(2*a)
    print("root1 = ",root1,"root2 = ",root2)
elif(discr==0):
    root1=root2=-b/(2*a)
    #root2=-b/(2*a)
    print("root1 = ",root1,"root2 = ",root2)
elif(discr<0):
    real=-b/(2*a)
    img=math.sqrt(-discr)/(2*a)
    print("root1 = ",real," - ",img,"i"," root2 = ",real," + ",img,"i")
