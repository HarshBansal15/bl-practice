dist=int(input("Enter dist"))
age=int(input("enter age"))
fare=dist*2
if age>60:
    fare=fare-fare*30/100
elif age<12:
    fare=fare-fare*50/100

print(fare)

