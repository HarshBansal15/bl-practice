a=[]
for i in range(5):
    n=int(input("Enter marks"))
    a.append(n)
flag=0
for i in range (5):
    if (a[i]<35):
        print("Fail")
        flag=1
        break;
if (flag==0):
    for i in range (5):
        if (a[i]>75):
            print("Distinction")
            flag=1
            break

if (flag==0):
    print("Pass")
    
    