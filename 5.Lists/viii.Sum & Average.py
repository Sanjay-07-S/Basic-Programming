#Find sum and average of numbers in a List in Python.


Element = input("Enter the Element: ")

number = list(map(int,Element.split()))

sum_element = sum(number)

average_element = sum_element / len(Element)

print("Sum of element: ",sum_element)
print("length of element: ",len(Element))
print("Average of element: ",average_element)