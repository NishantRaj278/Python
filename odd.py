N=str(input())
x=int(N[0])
y=int(N[-1])
w=x%2==0
z=y%2==0
if not w and not z:
    print("True")
elif not w and z:
    print("False")
elif w and not z:
    print("False")
else:
    print("True")