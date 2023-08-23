# Function calls
#  inputs (arguments) -> opertions ->  output (return value)
# Functions always take any number of arguments but there is always
# one value output.

def square(a):
    return a * a


def sub(a, b):
    return a - b


# print(square(3))
# square(5)
# print(sub(6, 4))
# print(sub(5, 9))


# We can also combine function calls with other operators including function calls

# print(sub(square(3),  square(1+1)))

''' 
How the above combination of function call executed.
1. square(3) - 9  
2.  9 and square(1+1) -> square(2)
3.  9 and square(2) -> 4
4.  sub(9 , 4) ->  5 answer
'''


# Function are object in python. if i print out the value of fuction square then python tells me
# it is a function

# print(square)  # <function square>

# To call a function we need parenthesis imediate after the name of funtion.
