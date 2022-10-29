x=float(input("enter the price of bike:"))
if x<=10000:
    if x>=5000:
        print("The selling price is:",x*25/100)
    else:
        print("The selling price is:",x*20/100)
elif x<=50000:
    if x>=35000:
        print("The selling price is:",x*50/100)
    elif x<35000 and x>=20000:
        print("The selling price is:",x*45/100)
    else:
        print("the selling price is:",x*40/100)
else:
    if x>100000:
        print("The selling price is:",x*90/100)
    elif x<=80000 and x>=60000:
        print("The selling price is:",x*80/100)
    else:
        print("the selling price is:",x*60/100)
