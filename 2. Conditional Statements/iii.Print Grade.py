#Print Grade based on marks
#Mark > 90 - print O grade
#Mark > 80 - print A grade
#Mark > 70 - print B grade
#Mark > 60 - print C grade
#Mark > 50 - print D grade
#Mark < 50 - print fail

Mark = int(input("Enter the Mark: "))
if Mark>100 or Mark<0:
    print("invalid")
elif Mark>90:
    print("O Grade")
elif Mark>80:
    print("A Grade")
elif Mark>70:
    print("B Grade")
elif Mark>60:
    print("C Grade")
elif Mark>50:
    print("D Grade")
elif Mark<50:
    print("Fail")
