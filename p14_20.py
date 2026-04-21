n=input("Enter number")
flag=0
for i in range(0,len(n)-1):
    if n[i]>n[i+1]:
        flag =1
        print('No')
        break

if flag==0:
    print ("Yes")


        
