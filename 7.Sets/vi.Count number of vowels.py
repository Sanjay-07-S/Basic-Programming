#Python program to count number of vowels using sets in given string
    #Input : Hello World
    #Output : No. of vowels : 3


vowels = set("aeiou")

String = input("Enter the string: ")
String = String.lower()
count_vowels = 0

for char in String:
    if char in vowels:
        count_vowels += 1
print("Number of vowels in string is : ",count_vowels)



