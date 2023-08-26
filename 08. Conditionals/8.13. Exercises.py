
# ======================================================
# Write code that asks the user to enter a numeric score (0-100). In response, it should print out the score and corresponding letter grade, according to the table below.
"""
  Score                  Grade
  >= 90                   A
  [80-90)                 B
  [70-80)                 C
  [60-70)                 D 
  < 60                    F

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 79.99999 gets grade C , but 80 gets grade B.
"""

#  ! Solution
"""

"""


# ======================================================
# A year is a leap year if it is divisible by 4; however, if the year can be evenly divided by 100, it is NOT a leap year, unless the year is also evenly divisible by 400 then it is a leap year. Write code that asks the user to input a year and output True if it’s a leap year, or False otherwise. Use if statements.
"""
Year              Leap?
1944              True
2011              False
1986              False
1800              False
1900              False
2000              True
2056              True

Above are some examples of what the output should be for various inputs.
"""


# ======================================================
# What do these expressions evaluate to?
"""
3 == 3
3 != 3
3 >= 4
not (3 < 4)
"""

# ======================================================
# Give the logical opposites of these conditions, meaning an expression that would produce False whenever this expression produces True, and vice versa. You are not allowed to use the not operator.
"""
a > b
a >= b
a >= 18  and  day == 3
a >= 18  or  day != 3
"""


# ======================================================
# Provided are the lengths of two sides of a right-angled triangle. Assign the length of the hypotenuse the the variable hypo_len. (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

# ======================================================
# Provided is a list of numbers. For each of the numbers in the list, determine whether they are even. If the number is even, add True to a new list called is_even. If the number is odd, then add False.

# ======================================================
# Provided is a list of numbers. For each of the numbers in the list, determine whether they are odd. If the number is odd, add True to a new list called is_odd. If the number is even, then add False.

# ======================================================
# Given the lengths of three sides of a triange, determine whether the triangle is right angled. If it is, the assign True to the variable is_rightangled. If it’s not, then assign False to the variable is_rightangled.

# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as

# if  abs(x - y) < 0.001:      # if x is approximately equal to y
# ...

# ======================================================

# Implement the calculator for the date of Easter.
# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.
# Ask the user to enter a year. Compute the following:
"""
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
dateofeaster = 22 + d + e
"""
# Special note: The algorithm can give a date in April. You will know that the date is in April if the calculation gives you an answer greater than 31. (You’ll need to adjust) Also, if the year is one of four special years (1954, 1981, 2049, or 2076) then subtract 7 from the date.
# Your program should print an error message if the user provides a date that is out of range.


"""

"""


# ======================================================
# Get the user to enter some text and print out True if it’s a palindrome, False otherwise. (Hint: Start by reversing the input string, and then use the == operator to compare two values to see if they are the same)


"""

"""

# ======================================================
# Write a program that will print out a greeting to each student in the list. This list should also keep track of how many students have been greeted and note that each time a new student has been greeted. When only one student has entered, the program should say “The first student has entered!”. Afterwards, the program should say “There are {number here} students in the classroom!”.

"""

"""

# ======================================================
#

"""

"""
