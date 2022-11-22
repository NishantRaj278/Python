import math
x=int(input())
y=int(input())
z=math.hypot(x,y)
w=z**3
v="{0:.3f}".format(w)
print(v)