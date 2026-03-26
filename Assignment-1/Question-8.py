#Question-8: Leap Year Checker

#Taking Year input
year=int(input("Enter Year: "))

#Checking leap year condition:
if year%4==0 and (year%100!=0 or year%400==0):
    print(year,"is a Leap year")
    if year % 400==0:
        print("Divisible by 400")
    else:
        print("Divisible by 4 and not divisible by 100")
else:
    print(year,"is Not a Leap Year")
    if year%100==0:
        print("Divisible by 100 but not by 400")
    else:
        print("Not divisible by 4")