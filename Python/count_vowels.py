word = input("Enter a word: ")
vowels = "aeiou"
count = 0

for letter in word.lower():
    if letter in vowels:
        count += 1

print("Number of vowels in the word:", count)