salary=int(input("Enter salary"))
late_days=int(input("Enter late"))
absent=int(input("Enter absent"))
salary=salary-(salary*5)/100 if late_days>5 and late_days<10 else salary-(salary*10)/100
if absent>=2:
    salary=salary-(salary*5)/100 
print(salary)

