import math
x=int(input())
y=int(input())
z=math.radians(x)
w=math.radians(y)
v=math.sin(z)*math.sin(w)-math.cos(z)*math.cos(w)
print("{0:.2f}".format(v))
