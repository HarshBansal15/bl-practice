n=input("Enter Number ")
sum=0
for i in range(len(n)):
    dig=int(n[i])
    sum=sum+dig**3
if int(n)==sum:
    print("Yes")
else:
    print("No")
