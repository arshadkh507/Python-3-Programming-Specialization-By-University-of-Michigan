# =============================================================
# ! 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
'''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
'''
# How I wonder what you are

"""
# ! Solution
print('''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
''')
# OR
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")
"""
# =============================================================

# ! 2. Write a Python program to find out what version of Python you are using.

"""
import sys
print("The Version of Python: " , sys.version)
print("The Version Info:")
print(sys.version_info)
"""

# =============================================================

# ! 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

""" 
import datetime
print(datetime.datetime.now())
"""

# =============================================================
# ! 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504
# Area of Circle = pi * r2

"""
from math import pi
radius = float(input("Enter radius of the Cricle :"))


def area_of_circle(radius):
    return pi * (radius * radius)


print("Radius of the  cirlce {} and it's Area {:.3f}".format(
    radius, area_of_circle(radius)))
"""

# =============================================================
# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# "Dany Boon"
# First and last name in reverse order
# "Boon Dany"

"""
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
"""

# ! OR

"""
user_name = input("Enter your first and last name: ")
user_name = user_name.split()
user_name.reverse()
print(" ".join(user_name))
"""

# =============================================================
# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

"""
comma_separated_numbers = input("Input some comma seprated numbers : ")
numbers_list = comma_separated_numbers.split(",")
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)
"""

# =============================================================
# ! 7 print extension of file name lefted


# =============================================================
# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]


"""
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))
"""


# =============================================================
# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

"""
exam_st_date = (11, 12, 2014)
(day, month, year) = exam_st_date
print("The examination will start from : {} / {} / {}".format(day, month, year))


# ! OR by w3resources

exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)
"""

# =============================================================
# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


"""
n = input("enter an integer: ")

# resultened_sum = (n + " " + n+n + " " + n+n+n).split()
# sum = 0
# for item in resultened_sum:
#     sum = sum + int(item)
# print(sum)

# ! OR
# print(n+n+n)
n1 = int(n)
n2 = int(n+n)
n3 = int(n+n+n)
print(n1 + n2 + n3)
"""

# =============================================================
