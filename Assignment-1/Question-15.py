#Question-15: Prime Number Checker

#Part 1: Check if a single number is prime. Handle negative numbers, 0, 1, and 2. 
num=int(input("Enter a number: "))
if num<=1:
    print(num,"is Not a prime number")
elif num==2:
    print("2 is a PRIME number")
else:
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,"is a prime number")
    else:
        print(num,"is NOT a prime number") 

#Part 2: Find all prime numbers in a given range  
start_range=int(input("Enter start range: "))
end_range=int(input("Enter end range: "))
print("Prime numbers are: ")
for n in range(start_range,end_range+1):
    if n>1:
        prime=True
        for i in range(2,n):
            if n%i==0:
                prime=False
                break
        if prime:
            print(n,end=",")