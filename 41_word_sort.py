# Python program to sort words in Alphabetic order

my_str =str(input("Enter the string :"))

words =[word.lower() for word in my_str.split()]

words.sort()

for word in words :
    print(word)