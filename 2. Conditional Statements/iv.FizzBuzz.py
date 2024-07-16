#write the program about the fizzbuzz
    # if the number is divisible by 3 print(Fizz)
    # if the number is divisible by 5 print(buzz)
    # if the number is divisible by 3 and 5 print(Fizzbuzz)


num = int(input("Enter The Number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num%3 ==0:
    print("Fizz")
elif num%5 ==0:
    print("Buzz")