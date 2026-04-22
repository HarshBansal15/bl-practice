n = int (input("Enter number"))

while n>10:
    s=0
    while n>0:
        a=n%10
        s=a+s
        n=n//10
    n=s

print(n)
