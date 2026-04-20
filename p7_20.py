n=int(input("Enter amount : "))
if n>=5000:
    n=n-(n*20)/100
elif n>=3000 and n<5000:
    n=n-(n*10)/100
elif n>=1000 and n<3000:
    n=n-(n*5)/100

print(f"Chal bhai tere {n} ka kaat gaya ")