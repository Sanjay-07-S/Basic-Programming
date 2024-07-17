#Check if element exists in list in Python.

Elements = input("Enter the Words: ")

Check_Element = input("Enter the Element To Check: ")

if Check_Element in Elements:
    print(f"Element '{Check_Element}' is Exists")

else:
    print(f"Element '{Check_Element}' is not exists")