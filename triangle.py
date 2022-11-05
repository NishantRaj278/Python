x=int(input("side1: "))
y=int(input("side2: "))
z=int(input("side3: "))
if x<y+z and y<x+z and z<x+y:
    print("possible")
else:
    print("not possible")