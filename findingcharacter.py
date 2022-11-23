str1=str(input())
char=str(input())
def find_char(str1,char):
    if char in str1:
        index=str1.index(char)
        print(index)
    else:
        print("not found")


find_char(str1,char)