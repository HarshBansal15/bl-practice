n=int(input("Enter first number"))
m=int(input("Enter second number"))
for i in range (n,m+1):
    is_prime=0
    for j in range (2,i):
        if(i%j==0): 
            is_prime=1
    if(is_prime==0): 
        print(i)        


