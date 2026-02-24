#Question-18: Calculator Functions

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Division by 0 is not allowed"
    return a/b
def modulus(a,b):
    return a%b
def power(a,b):
    return a**b
def calculator():
    while True:
        print("\nCalculator menu")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")
        print("6.Power")
        print("7.Exit")

        user_input=input("Enter input(1-7):")
        if user_input=="7":
            print("Exiting Calculator")
            break
        if user_input in ["1","2","3","4","5","6"]:
            a=float(input("Enter 1st number: "))
            b=float(input("Enter 2nd number: "))

            if user_input=="1":
                print("Result:",add(a,b))
            elif user_input=="2":
                print("Result:",subtract(a,b))
            elif user_input=="3":
                print("Result:",multiply(a,b))
            elif user_input=="4":
                print("Result:",divide(a,b))
            elif user_input=="5":
                print("Result:",modulus(a,b))
            elif user_input=="6":
                print("Result:",power(a,b))
        else:
            print("Invalid input")

#Run Calculator
calculator()