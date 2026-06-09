word = input("Enter a string: ")

reverse = ""

for char in word:
    reverse = char + reverse

if word == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
