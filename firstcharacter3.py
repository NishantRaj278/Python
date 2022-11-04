x={'1','2','3','4','5','6','7','8','9','0'}
y={'@','#','$','%','^','&','*'}
w=int(input())
v=str(w)
if v[-1] in x:
    print("digit")
elif v[-1] in y:
    print("character")