# Rearrange the code statements so that the program will add up the first n odd numbers where n is provided by the user.


# Write code to create a list of integers from 0 through 52 and assign that list to the variable numbers. You should use the Python range function and don’t forget to covert the result to a list – do not type out the whole list yourself.

mylist = []
for num in range(53):
    mylist = mylist + [num]

numbers = mylist
print(numbers)


# Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.


str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for count in str1:
    numbs = numbs + 1

print(numbs)


#  Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the total of the list’s values and assign that sum to the variable sum1.


numList = []
for i in range(41):
    numList = numList + [i]

numbers = numList

sum1 = 0
for n in numbers:
    sum1 = sum1 + n

print(sum1)
