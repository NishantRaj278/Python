BB=int(input("enter the cost of bike="))

if BB>100000:
    t1=int(15*BB/100)
    print("tax to be paid: ",t1)

elif BB>50000 and BB<=100000:
    t2=int(10*BB/100)
    print("tax to be paid: ",t2)

else:
    t3=int(5*BB/100)
    print("tax to be paid: ",t3)