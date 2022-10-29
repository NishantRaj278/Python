x=int(input("Enter a value:"))
y=x%2==0
if x>0 and y:
    print("It is an even number")
elif x>0 and not(y):
    print("It is a odd number")
else:
    print("It is negative number")

