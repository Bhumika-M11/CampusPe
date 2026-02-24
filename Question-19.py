#Question-19: Textv Analysis Functions

text=input("Enter text: ")
words=text.split()
vowels="aeiouAEIOU" #Defining vowels
word_count=len(words)

vowel_count=sum(1 for ch in text if ch in vowels)
consonant_count=sum(1 for ch in text if ch.isalpha() and ch not in vowels)
reversed_text=text[::-1]
palindrome=text.lower().replace(" ","")==text.lower().replace(" ","")[::-1]
no_vowels="".join(ch for ch in text if ch not in vowels)
longest=max(words,key=len)
frequency={}

for w in words:
    w = w.lower()          
    frequency[w] = frequency.get(w, 0) + 1   

# Displaying results
print("\n===TEXT ANALYSIS===")
print("Words: ",word_count)
print("Vowels: ",vowel_count)
print("Consonants: ",consonant_count)
print("Reversed: ",reversed_text)
print("Palindrome: ","Yes" if palindrome else "No")
print("Without vowels: ",no_vowels)
print(f"Longest word:{longest}({len(longest)}letters)")
print("Word Frequency: ",frequency)
