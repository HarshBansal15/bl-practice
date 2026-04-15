def add (a,b):
    print(a+b)
def sub (a,b):
    print(a-b)

a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=input("Enter operator + or - ")
if c== "+":
    add(a,b)
else:
    sub(a,b)
