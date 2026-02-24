#Question-14: Factorial Calculator

num=int(input("Enter number: "))

#Negative number 
if num<0:
    print("Factorial is not defined for negative number")

#0factorial
elif num==0:
    print("0!=1")

#Positive number
else:
    factorial=1
    steps=""
    for i in range(num,0,-1):
        factorial=factorial*i
        steps=steps+str(i)
        if i!=1:
            steps=steps+"x"
    print(f"{num}!={steps}={factorial}")