# =============================================================
# ! 1. Write a Python program to calculate the length of a string.

str1 = "A String Write a Python program to calculate the length of a string"
print("Problem 1 Solution: length of a string", len(str1))
# =============================================================
# ! 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

str2 = 'google.com'
char_frequency = 0
char_frequency_dictionary = {}
for char in str2:
    char_frequency = str2.count(char)
    char_frequency_dictionary = char_frequency_dictionary + \
        {char: char_frequency}

print(char_frequency_dictionary)
