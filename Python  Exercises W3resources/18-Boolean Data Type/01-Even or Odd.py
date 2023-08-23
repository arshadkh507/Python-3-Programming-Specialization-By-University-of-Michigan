
def even_or_odd(number):
    if number % 2 == 0:
        return number, " is Even"
    else:
        return number, " is Odd"

# ! OR


def is_even(number):
    return number % 2 == 0  # Return True or False.


print(even_or_odd(3))
