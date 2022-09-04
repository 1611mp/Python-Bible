# For loop implementation

vowels = 0
consonants = 0

for letter in "jinemeradillutiya jinemainumaarsutiya":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print(f"There are {vowels} vowels.")
print(f"There are {consonants} consonants.")