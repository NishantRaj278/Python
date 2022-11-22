import math
y=int(input())
x=math.radians(y)
cosec=1/math.sin(x)
sec=1/math.cos(x)
cot=1/math.tan(x)
print("{0:.2f}".format(cosec))
print("{0:.2f}".format(sec))
print("{0:.2f}".format(cot))
