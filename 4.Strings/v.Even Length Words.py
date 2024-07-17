#Python program to print even length words in a string

String = input("Enter the Words: ")

words = String.split()

print("Words In Even Length")

for word in words:
    if len(word)%2 ==0:
        print(word)



