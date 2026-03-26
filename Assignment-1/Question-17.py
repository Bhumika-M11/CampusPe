#Question-17: Palindrome Checker

text=input("Enter word/number: ")

#Original input text
original=text
#Reversing text
reversed_text=text[::-1]

print("Original: ",original)
print("Reversed: ",reversed_text)

#Checking palindrome
if text.lower()==reversed_text.lower():
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")