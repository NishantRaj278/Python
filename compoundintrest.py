p=int(input())
t=int(input())
r=float(input())
A=p*(1+r/100)**t
ci=A-p
x="{0:.2f}".format(ci)
print(x)