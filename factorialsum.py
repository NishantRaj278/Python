import math
x=int(input())
y=int(input())
sum=0
for i in range(x,y+1):
    sum=sum+math.factorial(i)
print(sum)
