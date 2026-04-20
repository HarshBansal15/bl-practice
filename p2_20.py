unit=int(input("Enter unit "))
unit1=unit
price=0
if (unit>0 and unit <=100):
    price=3*unit
elif (unit >100 and unit <=200):
    price=100*3
    unit=unit-100
    price=price+unit*5
elif (unit >200):
    price=100*3
    unit=unit-100
    price=price+100*5
    unit=unit-100
    price=price+unit*8

if unit1>300:
    price=price+price/10

print(price)
