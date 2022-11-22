import math
x=float(input())
if x>=-1 and x<=1:
    y=math.acos(x)
    print("{0:.4f}".format(y))
else:
    print("invalid")