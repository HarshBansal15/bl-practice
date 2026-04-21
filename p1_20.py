amount=int(input("Enter balance"))
n=int(input("Enter Number of trans"))
arr=[]
for i in range(n):
    x=int(input(f"Enter amount {i+1}th : "))
    arr.append(x)

for i in range (n):    
        if arr[i]%100==0 and amount>=arr[i] :
            print("Success")
            amount=amount-arr[i]
        else:
            print("Faaaaahhhhh")




