#Question-4: Age Calculator

from datetime import date
current_date=date.today() #Getting current day date

#Asking for birth year
birth_year=int(input("Enter birth year:"))
current_age=current_date.year-birth_year #Current age calculation

#Displaying Results
print("Approximate Age Calculation")
print("Current age:",current_age)
print("Age in months:",current_age*12)
print("Age in days:",current_age*365)
print("Age in hours:",current_age*365*24)
print("Age in minutes:",current_age*365*24*60)
print("Years until age 100:",100-current_age)