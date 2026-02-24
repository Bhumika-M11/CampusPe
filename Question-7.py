#Question-7: Temperature Converter

degree = chr(176) #Degree Symbol
while True:
    print("\n===Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice=int(input("Enter choice: ")) #Taking user choice
    if choice==7:
        print("Exiting Temperature Converter")
        break

    temp=float(input("Enter temperature: "))#Taking Temperature value

    if choice==1:
        result=(temp*9/5)+32
        print(f"Result: {result:.2f}{degree}F")

    elif choice==2:
        result=(temp-32)*5/9
        print(f"Result: {result:.2f}{degree}C")

    elif choice==3:
        result=temp+273.15
        print("Result:",result,"K")

    elif choice==4:
        result=temp-273.15
        print(f"Result: {result:.2f}{degree}C")

    elif choice==5:
        result=(temp-32)*5/9+273.15
        print("Result:",result,"K")

    elif choice==6:
        result=(temp-273.15)*9/5+32
        print(f"Result: {result:.2f}{degree}F")
    
    else:
        print("Invalid choice")