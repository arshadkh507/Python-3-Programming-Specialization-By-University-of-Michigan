
# 4. Write a Python function that checks if a given list is empty or not using boolean logic.


def is_list_empty(lst):
    if type(lst) != type([]):
        return "invalid input: Enter a list"
    return len(lst) == 0

# print(is_list_empty([]))

#   ! OR


def is_empty_list(lst):
    # print(not isinstance(lst, list))
    if not isinstance(lst, list):
        return "invalid input: Enter a list"
    return True


# print(is_empty_list([1]))


def is_empty_list(lst):
 # not bool(lst) if the list if empty bool(lst) will return False so we will return True that this is empty list to if condition and visa versa.
    return not bool(lst)


def main():
    try:
        input_list = eval(input("Input a list (e.g., [1, 2, 3, 4]): "))

        if isinstance(input_list, list):
            if is_empty_list(input_list):
                print("The list is empty.")
            else:
                print("The list is not empty.")
        else:
            print("Invalid input. Please enter a valid list.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
