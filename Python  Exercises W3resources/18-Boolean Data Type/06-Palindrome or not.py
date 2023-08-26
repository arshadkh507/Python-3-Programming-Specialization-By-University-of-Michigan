
# 6. Write a Python function that checks if a given string is a palindrome (reads the same backward as forward) using boolean values.

"""
def is_palindrom(str):
    reverse_str = ""
    for char in str:
        reverse_str = char.lower() + reverse_str

    if str.lower() == reverse_str:
        return True
    else:
        return False


input_str = input("Enter str to check for palindrome: ")

if isinstance(input_str, str):
    if is_palindrom(input_str):
        print(input_str, "  is a palindrom")
    else:
        print(input_str, " is not a palindrom")
else:
    print("Invalid input: please enter valid input e.g karak")
"""


# =====================================
# By w3Schoool

def is_palindrome(string):
    text = ''.join(char.lower() for char in string if char.isalnum())
    return text == text[::-1]  # text[::-1] reverse a string


# print(is_palindrome("11211")) # True
# ! isalnum() string methond that return ture if object is alphanumberic means A-Z and 0-9.
