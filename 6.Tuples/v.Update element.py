#Update each element in tuple list
	#The original list :[(1, 3, 4), (2, 4, 6), (3, 8, 1)]
	#Expected output - [(5, 7, 8), (6, 8, 10), (7, 12, 5)]



a = 1,3,4
b = 2,4,5
c = 3,8,1

original_list = [a,b,c]
print("Original List: ",original_list)

updated_list = [(a+4,b+4,c+4) for a,b,c in original_list]
print("Updated list: ",updated_list)