n=int(input("Enter no of bookings to be made :"))
a=[]
for i in range (n):
    m=int(input(f"Enter Number of seats required for booking number {i+1} "))
    a.append(m)
seats = 40
for i in range (n):
    seats = seats-a[i]
    if seats>0:
        print("Confirmed")
    else  :
        print("Waitlisted")
        seats=seats+a[i]
        

    

