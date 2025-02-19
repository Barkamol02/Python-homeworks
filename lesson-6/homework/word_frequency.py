try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print('"sample.txt" does not exist. Please provide a paragraph to create it.')
    user_input = input("Enter a paragraph: ")
    with open("sample.txt", "w") as file:
        file.write(user_input)
    print('"sample.txt" created successfully.')
    content = user_input

content = content.lower()

fresh_content = ""
for char in content:
    if char.isalnum() or char.isspace():
        fresh_content+=char
    else:
        fresh_content+=" "

words = fresh_content.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


n = int(input("How many top common word you want: "))
total_words = sum(word_count.values())
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
common_words = sorted_words[:n]

print(f"Total words: {total_words}")
print(f"Top {n} most common words:")
for word, number in common_words:
    print(f"{word} - {number} times")

with open("word_count_report.txt", "w") as file:
    file.write(f"Total Words: {total_words}\n")
    file.write(f"Top {n} Words:\n")
    for word, number in common_words:
        file.write(f"{word} - {number}\n")