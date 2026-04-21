n=int(input("Enter correct pin "))
flag =0
for i in range (3):
    a=int(input(f"Enter {i+1} /3 pin "))
    if a==n:
        flag+=1
        print("Correct")
        break

if (flag ==0):
    print("Locked")