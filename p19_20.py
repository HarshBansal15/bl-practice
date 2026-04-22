def palindrome (n):
    nn=0
    while n>0:
        a=n%10
        nn=nn*10+a
        n=n//10
    return nn
    
n=int(input("enter number"))
nn=palindrome(n)
print(f"Palindrom "if n==nn else "Not Palindrom" )
