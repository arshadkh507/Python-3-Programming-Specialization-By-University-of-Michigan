# =============================================================
# ! Write one for loop to print out each character of the string my_str on a separate line.
"""    
my_str = "MICHIGAN"
for char in my_str:
    print(char)
"""

# =============================================================
# ! Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

""" 
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for thing in several_things:
    print(thing)
for thing in several_things:
    print(type(thing))
"""
# =============================================================
# ! Write code that uses iteration to print out the length of each element of the list stored in str_list.

""" 
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for item in str_list:
    print(len(item))
# Write your code here.
"""
# =============================================================
# Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated, but draw something different than we have done in the past. (Hint: if you are drawing something complicated, it could get tedious to watch it draw over and over. Try setting .speed(10) for the turtle to draw fast, or .speed(0) for it to draw super fast with no animation.)

""" 

import turtle , random
window = turtle.Screen()
shape =  turtle.Turtle()
shape.speed(0)
shape.color("green")
shape.fillcolor("yellow")
shape.pensize(4)
for i in range(10):
    shape.hideturtle()  # make the turtle invisible
    shape.penup()  # don't draw when turtle moves
    shape.goto(0, -60)  # move the turtle to a location
    shape.showturtle()  # make the turtle visible
    shape.pendown()  # draw when the turtle moves
    for color in ["DarkGreen" ,  "DarkBlue" , "DarkSlateGray", "orange","brown","Chocolate", "Coral"]:
        angle = random.randrange(1,360)
        shape.color(color)
        shape.left(45)
        shape.forward(50)



"""
# =============================================================
# addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).

""" 
addition_str = "2+5+10+20"
addition_str = addition_str.split("+")
sum_val = 0

for num in addition_str:
    sum_val += int(num) 

"""


# =============================================================
# week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).
"""
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
avg_temp = 0
for temp in week_temps_f:
    avg_temp = avg_temp + float(temp)

week_temps_length = len(week_temps_f )
avg_temp =  avg_temp / week_temps_length

print(avg_temp)
"""

# =============================================================
# Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.
"""
nums = []
for n in range(68):
    nums = nums + [n]
    
print(nums)
"""
# =============================================================
