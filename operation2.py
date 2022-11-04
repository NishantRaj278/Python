x=int(input())
y=int(input())
z=str(input())
if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="//":
    print(x//y)
elif z=="%":
    print(x%y)
elif z=="**":
    print(x**y)
else:
    print("invalid")