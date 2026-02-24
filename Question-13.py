#Question-13: Sum and Average Calculator

num=int(input("How many numbers?"))
numbers=[]
#Taking numbers input
for i in range(num):
    n=int(input(f"Enter number {i+1}:"))
    numbers.append(n)

#Calculations
sum=sum(numbers)
average=sum/num
maximum=max(numbers)
minimum=min(numbers)

#Displaying Results
print("\n===Results===")
print("Sum: ",sum)
print("Average: ",average)
print("Maximum: ",maximum)
print("Minimum: ",minimum)