n=input("enter binary number")
a=0
nn=n[::-1]

for s in range(len(nn)):
    a=int(a)+int((2**s)*int(nn[s]))

print(a)