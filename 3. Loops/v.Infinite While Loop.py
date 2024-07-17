#Infinite While loop with a break statement to come out of loop.

while True:
    n = input("Enter Number or e-exit: ")
    if n == "e":
     print("Breaking The loop")
     break
try:
   n=int(n)
   print("You Entered: ",n)
except:
   print("")
  

