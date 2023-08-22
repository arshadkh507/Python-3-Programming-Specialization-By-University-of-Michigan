# =====================================================================
# ! Challenge-01
# Challenge: Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. Your program should output what the time will be on the clock when the alarm goes off.

# current_hours = input("Enter current time in hours:")
# current_hours = int(current_hours)

# waiting_hours = input("Enter number of hours to wait for alarm:")
# print("hours to wait for alarm: " + waiting_hours)
# waiting_hours = int(waiting_hours)


# total_hours = current_hours + waiting_hours
# time_on_clock = total_hours % 24


# time_state = 'am'

# if time_on_clock > 12:
#     time_state = 'pm'
# elif time_on_clock == 0:
#     time_state = 'mid night'
# else:
#     time_state = 'am'

# time_on_clock = time_on_clock % 12

# alarm_off_time = (str(time_on_clock) + time_state)

# print("******************************")
# print("\n\ncurrent time in hours: " + str(current_hours))
# print("hours to wait for alarm: " + str(waiting_hours))
# print("Alarm off timing: " + alarm_off_time)
# print("******************************")

# =====================================================================

# ! Challenge-02
# It is possible to name the days 0 thru 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6). Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.


# print('''Days Number
# 0: Sunday
# 1: Monday
# 2: Tuesday
# 3: Wednesday
# 4: Thrusday
# 5: Friday
# 6: Saturday
# ''')
# starting_day = input("Enter starting day number: ")
# starting_day = int(starting_day)

# stay_length = input("Enter stay days length in number: ")
# stay_length = int(stay_length)

# total_days = (starting_day + stay_length) % 7

# return_day = "Sunday"

# if total_days == 0:
#     return_day = 'day 0: Sunday'
# elif total_days == 1:
#     return_day = 'day 1: Monday'
# elif total_days == 2:
#     return_day = 'day 2: Tuesday'
# elif total_days == 3:
#     return_day = 'day 4: Wednesday'
# elif total_days == 4:
#     return_day = 'day 5: Thrusday'
# elif total_days == 5:
#     return_day = 'day 0: Friday'
# elif total_days == 6:
#     return_day = 'day 6: Saturday'
# else:
#     print(total_days)

# print("******************************")
# print("Starting day: ", starting_day)
# print("Stay days Length: ", stay_length)
# print("Total Days: ", total_days)
# print("Returning Day: ", return_day)
# print("******************************")

# =====================================================================
# ! Challenge-03
# Challenge: Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.

# str1 = "All "
# str2 = "work "
# str3 = "and "
# str4 = "no "
# str5 = "play "
# str6 = "makes "
# str7 = "Jack "
# str8 = "a "
# str9 = "dull "
# str10 = "boy"
# print(str1 + str2 + str3  +  str4 +  str5  +  str6  +  str7  +  str8  + str9  +  str10)

# =====================================================================
# ! Challenge-04
# Challenge: The formula for computing the final amount if one is earning compound interest is given on Wikipedia as
# A = P (1 + r / n)nt    # nt in power of (1 + r / n)
# where,
# P = principal amount (initial investment)
# r = annual nominal interest rate (as a decimal)
# n = number of times the interest is compounded per year
# t = number of years
# formula for compound interest
# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money will be compounded for. Calculate and print the final amount after t years.

'''
P = 10000  # assigns the principal amount of 10000 to variable P
n = 12     # assign to n the value 12
r = 0.08   # assign to r the interest rate of 8% (0.08)

t = int(input("Enter number of years in number: "))  # prompt the user for the number of years, t

A = P * ( 1 + r / n ) ** (n * t)

print(A)
'''

# =====================================================================
# ! Challenge-05
# Write a program that will compute the area of a circle. Prompt the user to enter the radius and save it to avariable called radius. Print a nice message back to the user with the answer.

'''
radius = int(input("Please Enter raduis of the circle: "))
pi = 3.14
area_of_circle =  pi * (radius ** 2)
print("Area of the circle is: " + str(area_of_circle))
'''


# =====================================================================
# ! Challenge-06
# Challenge: Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle and store the values in variables called width and height. Print a nice message with the answer.

'''
width = int(input("Enter width of rectangle: "))
height = int(input("Enter height of rectangle: "))
area_of_rectangle = width * height
print(area_of_rectangle)
'''

# =====================================================================
# ! Challenge-07
# Write a program that will compute MPG (Miles Per Gallon.) for a car. Prompt the user to enter the number of miles driven and store it in a variable called miles and the number of gallons used stored in a variable gallons. Print a nice message with the answer.
# Formula: Divide the distance in miles by the fuel amount in gallons.

'''
miles  =  int(input("Enter the number of miles driven: "))
gallons  =  int(input("Enter the number of gallons used: "))
MPG = miles / gallons
print(MPG)
'''

# =====================================================================
# ! Challenge-08
# Challenge: Write a program that will convert degrees celsius to degrees fahrenheit.
# Formula: °F = (°C × 9/5) + 32.

'''
celsius = input("Enter temperature in celsius degrees: ")
celsius = int(celsius)
fahrenheit = (celsius * 9/5) + 32.
print(fahrenheit)
'''
# =====================================================================
# ! Challenge-09
# Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. Calculate the equivalent temperature in degrees Celsius and store it in deg_c. Output a message to the user giving the temperature in Celsius.
# Formula: C = 5/9 (F-32)

'''
deg_f = int(input("Temperature in Fahrenheit: "))
deg_c = 5/9 * (deg_f-32)
print(deg_c)
  '''


# =====================================================================
# ! Challenge-10
# Write a program that will convert gallons to liters. This program will also need to get input from a user to see how many gallons should be converted and the result should be printed to the user.
# Drag and Drop question Answered in website

# =====================================================================
# ! Challenge-11
# Write a program that will convert tablespoons to teaspoons. This program will also need to get input from a user to see how many tablespoons should be converted and the result should be printed to the user.
# Drag and Drop question Answered in website
