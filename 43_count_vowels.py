# Python program to count the number of each vowel

vowels = 'aeiou'

my_str =str(input("Enter the string :"))

count ={}.fromkeys(vowels,0)

for char in my_str:
    if char in count:
        count[char] +=1

print(count)