#q1
name = str(input('What is your name?'))
year = int(input("Enter the year you were born "))
age = 2025 - year
print(f"{name} is {age} years old.")

#2     0123456789012
txt = 'LMaasleitbtui'
print(txt[1:3] + txt[5] + txt[7] + txt [9] + txt[11])
print(txt[0] + txt[3] + txt[4] + txt[6] + txt[8] + txt[12])

# #3
input12=str(input("Enter a string:"))
print(len(input12))
upperCase = input12.upper()
lowerCase = input12.lower()
print(upperCase)
print(lowerCase)

# #4
print(input12 == input12[::-1])

#5
string1 = "asdnbqwuWBEbaskd"
vowels = 'aeiouAEIOU'
count = sum(string1.count(vowel) for vowel in vowels)
print(count)
print(len(string1) - count)

# #6
print ('qw' in string1)

# #7
sentence = str(input("Input sentence: "))
replace = str(input("Replace: "))
newWord = str(input("With: "))
print(sentence.replace(replace, newWord))

#8
print(input12[0])
print(input12[-1])
    
# #9  
print(input12[::-1])  

# #10
print(len(sentence.split()))

# #11
print(any(char.isdigit() for char in input12))

#12
words =["apple", "banana", "cherry"]
separator = "-"
print(separator.join(words))

#13
print(input12.replace(" ", ""))

#14
string11 = input()
string12 = input()
print(string11 == string12)

#15
print("".join(word[0].upper() for word in sentence.split()))

#q16
input14 = str(input("Enter a string: "))
character11 = str(input("Enter a character to remove: "))
print(input14.replace(character11, ""))

#q17

print("".join("*" if char in vowels else char for char in input14))

#18
input18 = input("input a sentect:")
beginning = input("Enter the beginning of the sentence:")
ending = input("Enter the ending of the sentence:")
if input18.startswith(beginning) and input18.endswith(ending):
    print("True")
else:
    print("False")