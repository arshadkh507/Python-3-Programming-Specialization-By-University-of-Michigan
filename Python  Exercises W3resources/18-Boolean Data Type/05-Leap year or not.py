

# 5. Write a Python program that checks whether a given year is a leap year or not using boolean logic.

# If a year is divisible by 4 and not divisible by 100, it is a leap year.
# If a year is divisible by 100 but not divisible by 400, it is not a leap year.
# If a year is divisible by both 100 and 400, it is a leap year.

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False


input_year = int(input("Enter year in number: "))

if isinstance(input_year, int):
    if is_leap_year(input_year):
        print(input_year, " This is a leap year")
    else:
        print(input_year, " This is not a leap year")
else:
    print("Invalid input: please enter valid input e.g 2020")
