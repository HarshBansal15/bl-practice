def car_loan(principal , roi, years):
    n=years*12
    roi=roi/(12*100)
    montly=(principal*roi*(1+roi)**n)/((1+roi)**n-1)
    print(f"Your monthly payment is {montly:.2f}")

amount=int(input("Enter principal amount: "))
roi=int(input("Enter ROI: "))
years=int(input("Enter years: "))
car_loan(amount,roi,years)
