#Question-6: Grade Calculator

#Taking marks input in 5 subjects
m1=int(input("Enter marks for subject 1: "))
m2=int(input("Enter marks for subject 2: "))
m3=int(input("Enter marks for subject 3: "))
m4=int(input("Enter marks for subject 4: "))
m5=int(input("Enter marks for subject 5: "))

marks=[m1,m2,m3,m4,m5] #Storing marks in list

if any(mark<0 or mark>100 for mark in marks):
    print("Enter marks between 0 and 100")
else:
    #Displaying Marks in each subject 
    print("\nMarks in each subject:")
    for i in range(5):
        print(f"Subject {i+1}: {marks[i]}")
    
    #Total marks calculation
    total_marks=sum(marks) 
    #Percentage calculation
    percentage=(total_marks/500)*100 
    #Grade calculation
    if percentage>=90:
        grade="A+ (Outstanding)"
    elif percentage>=80:
        grade="A (Excellent)" 
    elif percentage>=70:
        grade="B (Good)"
    elif percentage>=60:
        grade="C (Average)"
    elif percentage>=50:
        grade="D (Pass)"
    else:
        grade="F (Fail)"
    
    #Result Calculation: Pass/Fail (Pass if all subjects >= 40) 
    if all(mark>=40 for mark in marks):
        result="Pass"
    else:
        result="Fail"
    
    #Displaying Results
    print("\n===Results===")
    print("Total marks:",total_marks,"/500")
    print(f"Percentage:{percentage:.2f}%")
    print("Grade:",grade)
    print("Result:",result)