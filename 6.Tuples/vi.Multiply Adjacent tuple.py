# Multiply Adjacent elements
#	The original tuple : (1, 5, 7, 8, 10)
#	Expected tuple after multiplication : (5, 35, 56, 80)


original_list = (1, 5, 7, 8, 10)
print("Original List: ",original_list)

product = []

for i in range(len(original_list) - 1):
    products = original_list[i] * original_list[i+1]
    product.append(products)
multiply_ele = tuple(product)
print(multiply_ele)