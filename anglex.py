import math
a=float(input("Opposite: "))
b=float(input("Hypotenuse: "))
c=a/b
x=math.asin(c)
deg=math.degrees(x)
print("{0:.2f}".format(deg))
