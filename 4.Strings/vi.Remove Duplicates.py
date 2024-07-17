#Remove All Duplicates from a Given String in Python

String = input("Enter the String: ")

duplicates = set()
result = " "

for char in String:
    if char not in duplicates:
        duplicates.add(char)
        result += char+" "
print(f"After Removed Duplicates: ",result)
    

