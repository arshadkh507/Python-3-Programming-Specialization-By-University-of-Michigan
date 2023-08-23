# Sometime it's necessary or convenient to convert values from one type to another
# For this Python have type conversion functions
# we called it Casting in python

# int() it convert other type of data if elligble to interger
# float() convert to float
# str() convert to string

# print(3.14,  int(3.14))  # result 3.14 3
#  ! int() it cutting off or discarded or truncated everything after the decimal points

# print(3.0, int(3.0)) # 3.0 3
# print(-3.0, int(-3.0))  # 3.0 3

# print("2345",  int("2345"))
# print(12,  int(12))

# print(int("12bottles")) # ! invalid literal for int() with base 10: '12bottles'

# Floats convert it into floating number float()
# String convert it into String  str()

# print("The value is " + 12)   # ! TypeError: can only concatenate str (not "int") to str
# print("The value is " + str(12))  # The value is 12
