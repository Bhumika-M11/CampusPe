#Question-3: String Manipulator

#Asking user for a sentence
sentence=input("Enter a sentence:")

words=sentence.split() #Splitting sentences into words

#Dsplaying Results
print("Original:",sentence)
print("Characters (with spaces):",len(sentence))
print("Characters (without spaces):",len(sentence.replace(" ","")))
print("Words:",len(words))
print("UPPERCASE:",sentence.upper())
print("lowercase:",sentence.lower())
print("Title Case:",sentence.title())
print("First word:",words[0])
print("Last word:",words[-1])
print("Reversed:",sentence[::-1])