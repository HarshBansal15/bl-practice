n=int(input("Enter how many inflow "))
a=[]
flag =0
quant=1000
for i in range (n):
    m=int(input("Enter Quantity "))
    a.append(m)
for i in range (n):
    quant=quant-a[i]
    if quant<0:
        print(f"overflow : {i+1}")
        flag+=1
        break
if flag ==0:
    print("not filled")
