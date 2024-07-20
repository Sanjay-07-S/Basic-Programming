#Find the size of a tuple in bytes.

import sys

Element = input("Enter the Elements: ")

size = tuple(Element)

tuple_size = sys.getsizeof(size)

print("Size of the tuple in bytes: ",tuple_size)