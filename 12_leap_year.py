#  Python program to check leap year

for i in range(10):
    year =int(input("Enter the year : "))
    #for year<=1582:
        #print("Year must be greater than 1582")
    if (year%400==0) and (year%100==0) :
        print(year,"is a leap year")
    elif (year%4==0) and (year%100!=0):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")