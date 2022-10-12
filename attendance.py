N1=int(input("Enter number of classes attended:"))
N2=int(input("Enter number of classes held:"))

per=N1*100/N2

if per>=75:
    print("The student is allowed to take exam")

else:
    print("The student is not allowed to take exam")