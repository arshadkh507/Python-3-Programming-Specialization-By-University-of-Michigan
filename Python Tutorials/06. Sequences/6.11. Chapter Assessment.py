# Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write your code so that it works no matter how many items are in the list.


#  MCQS  What is the type of a?
b = "My, what a lovely day"
x = b.split(',')
print(x)
z = "".join(x)
y = z.split()
a = "".join(y)
print(type(a))


# Write code to determine how many 9’s are in the list nums and assign that value to the variable how_many. Do not use a for loop to do this.
nums = [4, 2, 23.4, 9, 545, 9, 1, 234.001, 5, 49, 8, 9, 34, 52, 1, -2, 9.1, 4]
how_many = nums.count(9)
