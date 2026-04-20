s=input("Enter password : ")
upper=0
digit=0
for i in range(len(s)):
    if(s[i].isupper()):
        upper+=1
    if(s[i].isdigit()):
        digit+=1

if upper>0 and digit>0 and len(s)>=8:
    print("Strong")
else:
    print("Change kar le weak hai ")

