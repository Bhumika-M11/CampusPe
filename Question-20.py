#Question-20: Number System Functions

def factorial(n):
    f=1
    i=1
    while i<=n:
        f=f*i
        i=i+1
    return f

def is_prime(n):
    if n<=1:
        return False
    i=2
    while i<n:
        if n%i==0:
            return False
        i=i+1
    return True

def fibonacci(n):
    a=0
    b=1
    i=1
    while i<n:
        c=a+b
        a=b
        b=c
        i=i+1
    return a

def sum_of_digits(n):
    s=0
    while n>0:
        s=s+(n%10)
        n=n//10
    return s

def reverse_number(n):
    rev=0
    while n>0:
        rev=rev*10+(n%10)
        n=n//10
    return rev


def is_armstrong(n):
    temp=n
    count=0
    while temp>0:
        count=count+1
        temp=temp//10
    temp=n
    total=0
    while temp>0:
        d=temp%10
        total=total+(d**count)
        temp=temp // 10

    return total==n

def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

def is_perfect_number(n):
    i=1
    s=0
    while i<n:
        if n%i==0:
            s=s+i
        i=i+1
    return s==n

def math_menu():
    while True:
        print("\n===Math Menu===")
        print("1.Factorial")
        print("2.Prime Check")
        print("3.Fibonacci")
        print("4.Sum of Digits")
        print("5.Reverse Number")
        print("6.Armstrong Check")
        print("7.GCD")
        print("8.LCM")
        print("9.Perfect Number Check")
        print("10.Exit")
        
        choice=int(input("Enter choice: "))

        if choice==1:
            n=int(input("Enter number: "))
            print("Factorial:",factorial(n))

        elif choice==2:
            n=int(input("Enter number: "))
            print("Prime:",is_prime(n))

        elif choice==3:
            n=int(input("Enter number: "))
            print("Fibonacci:",fibonacci(n))

        elif choice==4:
            n=int(input("Enter number: "))
            print("Sum of digits:",sum_of_digits(n))

        elif choice==5:
            n=int(input("Enter number: "))
            print("Reversed number:",reverse_number(n))

        elif choice==6:
            n=int(input("Enter number: "))
            print("Armstrong:",is_armstrong(n))

        elif choice==7:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("GCD:",gcd(a, b))

        elif choice==8:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("LCM:",lcm(a, b))

        elif choice==9:
            n=int(input("Enter number: "))
            print("Perfect Number:", is_perfect_number(n))

        elif choice==10:
            print("Exiting")
            break
        else:
            print("Invaild choice")
#Run
math_menu()           