# ===========================================================
#! In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop tries to output these names in order.
# Of course, that’s not quite right because Ouack and Quack are misspelled. Can you fix it?

'''
prefixes = "JKLMNOPQ"
suffix = "ack"
suffix2 = "uack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + suffix2)
    else:
        print(p + suffix)
'''

# ===========================================================
# ! Get the user to enter some text and print it out in reverse order.

'''
user_input = input("Enter some text to print in reverse order:")

new_str = ""
count = len(user_input) - 1

for i in range(len(user_input)):
    new_str = new_str + user_input[count - i]

print(new_str)
'''

# ===========================================================
# ! Write a program that uses a for loop to print
# One of the months of the year is January
# One of the months of the year is February
# One of the months of the year is March
# etc …

import turtle
months_list = ["January", "February", "March"]
for month in months_list:
    print("One of the months of the year is " + month)


# ===========================================================
# ! Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99, 20
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.

'''
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for num in numbers:
    print(num)
    
for num in numbers:
    print(num, num ** 2)
'''
# ===========================================================
# ! Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon. The program should draw the polygon and then fill it in.
number_of_sides = int(input("Enter number of sides:"))
Length_of_side = int(input("Enter Length of side:"))
color_of_polygon = input("Enter color of polygon:")
fillcolor_of_polygon = input("Enter fill color of a regular polygon:")

window = turtle.Screen()
polygon = turtle.Turtle()
polygon.color(color_of_polygon)
polygon.fillcolor(fillcolor_of_polygon)

for i in range(number_of_sides):
    polygon.forward(Length_of_side)
    polygon.left(360 // number_of_sides)

window.exitonclick()


# ===========================================================
# A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading. Assume that the turtle originally has a heading of 0 and accumulate the changes in heading to print out the final. Your solution should work for any sequence of experimental data.


# Initialize the turtle
wn = turtle.Screen()
pirate = turtle.Turtle()

# Experimental data
turn_angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

# Initialize variables
current_heading = 0

# Iterate through the turn angles
for angle in turn_angles:
    pirate.left(angle)  # Turn by the specified angle
    pirate.forward(100)  # Take 100 steps forward
    current_heading += angle  # Update the current heading

# Print the final heading
print("Final Heading:", current_heading)

# Close the turtle window on click
wn.exitonclick()

# ===========================================================
