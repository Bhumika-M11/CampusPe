#Question-16.py: Number Guessing Game

import random
num=random.randint(1,100)
for i in range(7):
    g=int(input("Guessing Number: "))
    if g==num:
        print("Correct")
        break
    elif g<num:
        print("Too Low")
    else:
        print("Too High")
else:
    print("Number was:",num)