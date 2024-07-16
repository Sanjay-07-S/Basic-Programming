#Infinite While loop with a break statement to come out of loop.

while True:
    n = input("Enter Number or b-quit: ")
    if n == "b":
     print("Breaking The loop")
     break
try:
   n=int(n)
   print("You Entered: ",n)
except:
   print("")
  

