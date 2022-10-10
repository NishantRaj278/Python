import keyword
keys=["global","rain","Ukraine","True","False","Yash","except"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i]+" is a keyword")

    else:
        print(keys[i]+" is not a keyword")    

