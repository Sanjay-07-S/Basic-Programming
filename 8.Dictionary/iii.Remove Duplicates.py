#Remove all duplicates from a given sentence
    #Input : Python is great and Java is also great
    #Output : python is great and java also

sentance = input("Enter the Sentence: ")

input = sentance.split()

input_dict = {}

for word in input:
    input_dict[word] = None

    end = " ".join(input_dict.keys())


print("Sentence after removing duplicates: ",end)