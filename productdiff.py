x=int(input("num1: "))
y=int(input("num2: "))
w=str(x)
v=str(y)
a=int(w[0])**2*int(w[1])**2
b=int(v[0])**2*int(v[1])**2
z=a-b
if z>0:
    print("P")
elif z==0:
    print("Z")
elif z<0:
    print("N")
else:
    print("invalid")