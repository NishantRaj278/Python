import math
a=int(input())
b=int(input())
c=int(input())
if math.hypot(a,b)==c:
    print(c**2)
else:
    print("not satisfied")