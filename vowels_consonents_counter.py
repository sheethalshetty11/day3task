string = input("Enter text: ")

vowel_count = 0
consonant_count = 0

for letter in string:
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1

print("Number of vowels =", vowel_count)
print("Number of consonants =", consonant_count)
