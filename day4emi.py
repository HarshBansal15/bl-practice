# PROG 4.2: EMI Utility Functions

# Function to calculate Interest
def calculate_interest(principle, roi, frequency=12):
    return round(principle * roi / (frequency * 100), 2)


# Function to calculate EMI
def calculate_emi(principle, roi, time):
    # Step 1: Monthly interest rate
    interest_per_month = calculate_interest(1, roi)

    # Step 2: Number of months
    months = time * 12

    # Step 3: EMI formula
    emi = (principle * interest_per_month * (1 + interest_per_month) ** months) / \
          ((1 + interest_per_month) ** months - 1)

    # Step 4: Return EMI
    return emi


# PROG 4.3: Compute EMI Details

def compute_emi_details(principle, roi, time):
    
    # Step 1: Initialize list
    emi_details = []

    # Step 2: Calculate EMI
    emi = calculate_emi(principle, roi, time)

    # Step 3: Initialize balance
    balance = principle

    # Step 4: Loop through months
    for month in range(1, time * 12 + 1):

        # Step 5: Dictionary for each month
        emi_dict = {}

        # Step 6: Calculate values
        interest = calculate_interest(balance, roi, 12)
        principal = emi - interest
        balance = balance - principal

        # Step 7: Handle negative balance
        if balance < 0:
            principal = round(principal + balance, 2)
            emi = round(principal + interest, 2)
            balance = 0

        # Step 8: Store values
        emi_dict["Month"] = month
        emi_dict["EMI"] = round(emi, 2)
        emi_dict["Interest"] = round(interest, 2)
        emi_dict["Principal"] = round(principal, 2)
        emi_dict["Balance"] = round(balance, 2)

        # Step 9: Append to list
        emi_details.append(emi_dict)

    # Step 10: Return list
    return emi_details


# Test the function
pa=int(input("Enter amount "))
roi=int(input("Enter roi "))
time=int(input("Enter time "))
emi_details = compute_emi_details(pa, roi, time)

print("EMI Details:")
for emi_dict in emi_details:
    print(emi_dict)


# # Convert to JSON format
# import json

# emi_details_json = json.dumps(emi_details)

# print("\nJSON Payload:")
# print(json.dumps(json.loads(emi_details_json), indent=2))