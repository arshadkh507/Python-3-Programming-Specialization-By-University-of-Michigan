
# 9.15. Exercises
# =============================================================
# For each word in the list verbs, add an -ing ending. Overwrite the old list so that verbs has the same words with ing at the end of each one.

"""
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
for index in range(len(verbs)):  
    verbs[index] = verbs[index] + "ing"
    
print(verbs)
"""

# =============================================================
# In XYZ University, upper level math classes are numbered 300 and up. Upper level English classes are numbered 200 and up. Upper level Psychology classes are 400 and up. Create two lists, upper and lower. Assign each course in classes to the correct list, upper or lower. HINT: remember, you can convert some strings to different types!

"""

classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper  = []
lower = []
for cls in classes:
    num_of_cls = cls.split()
    subject = num_of_cls[0]
    number = int(num_of_cls[1])
    if subject == "MATH" and number >= 300:
        upper.append(cls)
    elif subject == "ENG" and number >= 200:
        upper.append(cls)
    elif subject == "PSYCH" and number >= 400:
        upper.append(cls)
    else:
        lower.append(cls)
        
print(upper)
print(lower)

"""
# =============================================================
# Starting with the list myList = [76, 92.3, ‘hello’, True, 4, 76], write Python statements to do the following:

# Append “apple” and 76 to the list.
# Insert the value “cat” at position 3.
# Insert the value 99 at the start of the list.
# Find the index of “hello”.
# Count the number of 76s in the list.
# Remove the first occurrence of 76 from the list.
# Remove True from the list using pop and index.


"""
myList = [76, 92.3, 'hello', True, 4, 76]
myList.append("apple")
myList.append(76)
myList.insert(3, "cat")
myList.insert(0, 99)
hello_index = myList.index("hello")
count_76 = myList.count(76)

# Find and remove the first occurrence of 76
if 76 in myList:
    myList.remove(76)

# Find and remove True using pop and index
if True in myList:
    index_true = myList.index(True)
    myList.pop(index_true)

print(myList)

"""
# =============================================================
# The module keyword determines if a string is a keyword. e.g. keyword.iskeyword(s) where s is a string will return either True or False, depending on whether or not the string is a Python keyword. Import the keyword module and test to see whether each of the words in list test are keywords. Save the respective answers in a list, keyword_test.

"""
import keyword
test = ["else", "integer", "except", "elif"]
keyword_test = []
for item in test:
    if keyword.iskeyword(item):
        keyword_test.append(True)
    else: 
        keyword_test.append(False)
        
"""

# =============================================================
# The string module provides sequences of various types of Python characters. It has an attribute called digits that produces the string ‘0123456789’. Import the module and assign this string to the variable nums. Below, we have provided a list of characters called chars. Using nums and chars, produce a list called is_num that consists of tuples. The first element of each tuple should be the character from chars, and the second element should be a Boolean that reflects whether or not it is a Python digit.

"""
import string
chars = ['h', '1', 'C', 'i', '9', 'True', '3.1', '8', 'F', '4', 'j']
nums = string.digits
print(nums)
is_num = []

for char in chars:
    if char in nums:
        is_num.append((char, True))
    else:
        is_num.append((char, False))  
"""
# =============================================================
"""

"""
# =============================================================
"""

"""
# =============================================================
"""

"""
# =============================================================
"""

"""
# =============================================================
"""

"""
# =============================================================
"""

"""
