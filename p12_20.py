a=input("enter string")
count=0
for i in a:
    # if (a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U' or a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' ):
        if i in "aeiouAEIOU":
            count +=1
print (count) 