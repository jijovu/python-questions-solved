# Python program to check whether a string is Palindrom or Not

a =str(input("Enter a palindrom :"))

a =a.casefold()

rev_a=reversed(a)

if list(a)==list(rev_a):
    print("String is a palindrom")
else:
    print("String is not a palindrom")







