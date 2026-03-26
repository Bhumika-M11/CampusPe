#Question-9: Ticket Pricing System

#Taking input from user
age=int(input("Enter age: "))
day=input("Enter day of week: ").lower()
tickets=int(input("Enter number of tickets: "))

#Age-Based price calculation
if age<3:
    base_price=0
    category="Free Ticket"
elif 3<= age <=12 :
    base_price=150
    category="Child Ticket"
elif 13<= age <=59 :
    base_price=300
    category="Adult Ticket"
else:
    base_price=200
    category="Senior Ticket"

#Day-based Discount
if day in ["friday","saturday","sunday"]:
    discount_rate=0.20
else:
    discount_rate=0

#Calculations
base_amount=base_price*tickets
discount_amount=base_amount*discount_rate
final__amount=base_amount-discount_amount

#Displaying Results
print("\n===Movie Ticket===")
print("Category: ",category)
print("Base price: ₹",f"{base_price:.2f}")
print("Base Amount: ₹",f"{base_amount:.2f}")
print("Discount: ₹", discount_amount)
print("Total amount: ",final__amount)