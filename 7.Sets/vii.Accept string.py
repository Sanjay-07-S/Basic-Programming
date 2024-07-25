#Python Program to Accept the Strings Which Contains all Vowels
    #Input : ABeeIghiObhkUul
    #Output : Accepted
        #All vowels are present

vowels = set("aeiou")

String = input("Enter the string: ").lower()

String= set(String)

Contains_all_vowels = vowels.issubset(String)
if Contains_all_vowels == True:
    print ("Accepted")
    print("All vowels are present")
else:
    print("Not Accepted")
    print("Not all vowels are present")







