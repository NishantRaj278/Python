a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))
for i in (a,b,c,d):
    if i%5==0 and i%3==0:
        print(i)