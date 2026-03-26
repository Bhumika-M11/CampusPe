#Question-12: Multiplication Table Generation

number=int(input("Enter number: "))
range_end=int(input("Enter range(end): "))

print(f"\nMultiplication Table of {number}")
for i in range(1,range_end+1):
    print(f"{number}x{i}={number*i}")

#Full multiplication table
print(f"\nMultiplication Table (1-10)")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()