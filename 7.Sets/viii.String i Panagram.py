#Python set to check if a String is a panagram
    #Input : The quick brown fox jumps over the lazy dog
    #output : The string is a panagram

String = input("Enter the Sentence: ").lower()
String = set(String)

Alphabets_String = set("abcdefghijklmnopqrstuvwxyz")

panagram = Alphabets_String.issubset(String)

if panagram==True:
    print("String is a Panagram")
else:
    print("String is Not Panagram")