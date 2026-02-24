#Question-11: Number Pattern Printer

print("Choose Pattern: ")
print("Pattern 1")
print("Pattern 2")
print("Pattern 3")
print("Pattern 4")
pattern=int(input("Enter pattern: "))
h=int(input("Enter height: "))

#Pattern 1
if pattern==1:
    for i in range(1,h+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

#Pattern 2
elif pattern==2:
    for i in range(1,h+1):
        for j in range(i):
            print(i,end=" ")
        print()

#Pattern 3
elif pattern==3:
    for i in range(h,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

#Pattern 4
elif pattern==4:
    for i in range(1,h+1):
        print(" "*(h-i),end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
else:
    print("Invaild pattern")