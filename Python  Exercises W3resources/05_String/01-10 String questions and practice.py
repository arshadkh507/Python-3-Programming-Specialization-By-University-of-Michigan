# =============================================================
# ! 1. Write a Python program to calculate the length of a string.

str1 = "A String Write a Python program to calculate the length of a string"
# print("Problem 1 Solution: length of a string", len(str1))

# =============================================================
# ! 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

"""
str2 = 'google.com'
char_frequency = 0
char_frequency_dictionary = {}
for char in str2:
    char_frequency = str2.count(char)
    char_frequency_dictionary = char_frequency_dictionary + \
        {char: char_frequency}

print(char_frequency_dictionary)
"""

# =============================================================
#  3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

"""
input_str = input("Enter a string: ")

def first_last_2_chars(str):
    if len(str.strip()) < 2:
        return ""

    return str[:2] + str[-2:]

# print(first_last_2_chars("  "))
print(first_last_2_chars(input_str))
"""

# =============================================================
# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

"""
def first_char_change(str):
    indexes = []
    count = 0

    if len(str.strip()) <= 1:
        return "String is too short"

    for char in str:
        if char == str[0]:
            indexes.append(count)
        count = count + 1

    change_str = ""
    for n in range(len(str)):
        if n != 0 and n in indexes:
            change_str = change_str + "$"
        else:
            change_str = change_str + str[n]

    return change_str


# print(first_char_change("arshad"))  # arsh$d
# print(first_char_change("restart"))  # resta$t



# ! W3resources
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char('restart'))

"""

# =============================================================
# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

"""
def chars_mix_up(str1, str2):
    if len(str1) <= 1 or len(str2) <= 1:
        return "String too short"
    new_a = str2[:2] + str1[2:]
    new_b = str1[:2] + str2[2:]
    return new_a + " " + new_b


print(chars_mix_up('abc',  "xyz"))  # xyc abz
"""

# =============================================================
# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

"""
def add_ing(str):
    if len(str) < 3:
        return str
    elif str.endswith('ing'):
        return str + 'ly'
    else:
        return str + 'ing'


# print(add_ing("arshad")) # arshading
# print(add_ing("abc"))  # abcing
# print(add_ing("string"))  # stringly
"""

# =============================================================
#  7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


"""

"""

# =============================================================
# 8. Write a Python function that takes a list of words and returns the length of the longest one.

"""
def longest_word(words_list):
    long_word_length = 0
    long_word = ""
    for word in words_list:
        if len(word) > long_word_length:
            long_word_length = len(word)
            long_word = word

    return "Longest word {} and it's length is {}.".format(long_word, long_word_length)


# Longest word Exercises and it's length 9.
print(longest_word(["PHP", "Exercises", "Backend",
      "arshad khan", "Exercises12", "Backend12345", "arshad khan"]))


! W3resources solutionn

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]
    
# [(3, 'PHP'), (9, 'Exercises'), (7, 'Backend')]
# [(3, 'PHP'), (7, 'Backend'), (9, 'Exercises')]
print(find_longest_word(["PHP", "Exercises", "Backend"]))
"""


# =============================================================
#


"""

"""

# =============================================================
#


"""

"""

# =============================================================
#
