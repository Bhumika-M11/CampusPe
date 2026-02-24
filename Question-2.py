#Question-2: Simple Calculator

#Taking input 
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))

#Performing Calculations
Add=n1+n2 #Addition
Sub=n1-n2 #Subtraction
Mul=n1*n2 #Multiplication

if n2!=0:
    Div=n1/n2 #Divsion
    Mod=n1%n2 #Modulus
else:
    Div=None
    Mod=None

Exp=n1**n2 #Exponentiation

#Displaying Results
print("Results:")
print(f"{n1:.0f} + {n2:.0f} = {Add:.0f}")
print(f"{n1:.0f} - {n2:.0f} = {Sub:.0f}")
print(f"{n1:.0f} * {n2:.0f} = {Mul:.0f}")
if Div is not None:
    print(f"{n1:.0f} / {n2:.0f} = {Div:.2f}") 
    print(f"{n1:.0f} % {n2:.0f} = {Mod:.0f}")
else:
    print("Divison by 0 is not allowed")
    print("Modulus by 0 is not allowed")
print(f"{n1:.0f} ** {n2:.0f} = {Exp:.0f}")