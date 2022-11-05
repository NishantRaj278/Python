s=float(input())
x=4*s
w="{0:.2f}".format(x)
y=s**2
v="{0:.2f}".format(y)
if s<10:
    print(v)
else:
    print(w)