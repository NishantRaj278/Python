import math
x=int(input())
if x>360:
    print("enter a valid angle")
else:
    print(format(math.degrees(x),".5f"))