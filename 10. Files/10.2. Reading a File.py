
# ! open() File

fileref = open("readingfile.txt", "r")  # r read the file
print(fileref)  # <_io.TextIOWrapper name='readingfile.txt' mode='r' encoding='cp1252'>

# ! read()
# contents = fileref.read()

# ! readlines()
# lines = fileref.readlines()
# print(lines[:4])

# print(isinstance(lines, list))  # True

# count = 0
# for line in lines[:4]:
#     count = count + 1
#     print(line.strip())

# ! we can directly itrate over the lines. it is a common way
# for line in fileref:
#     print(line.strip())

# ! close() the operation


f = open("readingfile.txt", "r")
txt = f.readline()
print(txt)

fileref.close()
# =====================================================
# Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
'''
file = open("travel_plans2.txt", "r")
lines = file.readlines()
num_lines = len(lines)
print(num_lines)
file.close()
'''

# =====================================================
# Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.
'''
file = open("school_prompt2.txt",  "r")
contents = file.read()
num_char = len(contents)
print(num_char)
file.close()
'''
# =====================================================
# Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.
'''
file = open("emotion_words2.txt", "r")
first_forty = file.read(40)
print(first_forty)
file.close()
'''

# =====================================================

# Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

''' 
file = open("emotion_words.txt", "r")
num_lines = 0
for aline in file:
    num_lines = num_lines + 1
file.close()
print(num_lines)
'''
