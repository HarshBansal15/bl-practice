# PROG 6: Bill Generation App (Final Combined)

APPLE_GST = 0.12
ORANGE_GST = 0.05
buyer_name = input("Enter Buyer Name: ")

apple_price = int(input("Enter Apple price per kg: "))
apple_qty = float(input("Enter Apple quantity in kg: "))

orange_price = int(input("Enter Orange price per kg: "))
orange_qty = float(input("Enter Orange quantity in kg: "))

apple_total = apple_price * apple_qty
orange_total = orange_price * orange_qty

apple_gst = apple_total * APPLE_GST
orange_gst = orange_total * ORANGE_GST

apple_final = apple_total + apple_gst
orange_final = orange_total + orange_gst

total_amount = apple_final + orange_final
rounded_total = round(total_amount, 2)

print("\n" + "="*70)
print(f"{'BILL RECEIPT':^70}")
print("="*70)

print(f"Buyer Name: {buyer_name}")
print("-"*70)

print(f"| {'Item':^10} | {'Price':^10} | {'Qty':^10} | {'Total':^10} | {'GST':^10} | {'Final':^10} |")
print("-"*70)

print(f"| {'Apple':<10} | {apple_price:>10} | {apple_qty:>10} | {apple_total:>10.2f} | {apple_gst:>10.2f} | {apple_final:>10.2f} |")

print(f"| {'Orange':<10} | {orange_price:>10} | {orange_qty:>10} | {orange_total:>10.2f} | {orange_gst:>10.2f} | {orange_final:>10.2f} |")

print("-"*70)

print(f"{'Total Amount':<50}: ₹ {total_amount:.2f}")
print(f"{'Rounded Total':<50}: ₹ {rounded_total:.2f}")

print("="*70)