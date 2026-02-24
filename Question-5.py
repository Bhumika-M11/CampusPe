#Question-5: Bill Splitter
#Inputs
total_bill=float(input("Enter total bill:"))
people=int(input("Number of people:"))
tax_percent=float(input("Tax percentage:"))
tip_percent=float(input("Tip percentage:"))

#Calculations
if people<=0:
    print("Number of people must be greater than 0")
else:
    subtotal=total_bill
    tax_amount=subtotal*(tax_percent/100)
    after_tax=subtotal+tax_amount
    tip_amount=after_tax*(tip_percent/100)
    total_amount=after_tax+tip_amount
    per_person=total_amount/people

    #Displayig bill
    print("\n===BILL BREAKDOWN===")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax({tax_percent:.0f}%): ₹{tax_amount:.2f}")
    print(f"Afetr tax: ₹{after_tax:.2f}")
    print(f"Tip({tip_percent:.0f}%): ₹{tip_amount:.2f}")
    print(f"Total: ₹{total_amount:.2f}")
    print(f"Per Person: ₹{per_person:.2f}")