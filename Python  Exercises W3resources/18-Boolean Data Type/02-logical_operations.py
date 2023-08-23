
# ! 2. Write a Python function that takes two boolean values as input and returns the logical AND and OR of those values.

def logical_operations(bool_value1, bool_value2):
    logical_and = bool_value1 and bool_value2
    logical_or = bool_value1 or bool_value2

    return logical_and, logical_or


# print(logical_operations(True, False))
