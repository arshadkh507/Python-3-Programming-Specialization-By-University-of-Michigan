
# 7. Write a Python program that implements a program that validates a user's password based on certain criteria (length, containing numbers and special characters etc.) using boolean expressions.


def is_valid_password(password):
    special_chars = '''!"#$%&' ()*+,-./:;<=>?@ []^_` {|}~"'''

    if len(password) < 8 or len(password) > 16:
        return "invalid password: password length must be between 8 and 16 characters"
    elif special_chars not in password:
        return "invalid password: password must be contains special characters"
    elif not password.isalnum():
        return "invalid password: password must be contains numbers"
    else:
        return "password is valid"


input_password = input("Enter password to check it's validatioin: ")


print(is_valid_password(input_password))


# ===================================================

def Is_password_valid(password):
    # Check if password length is between 8 and 16 characters
    if len(password) < 8 or len(password) > 16:
        return False

    # Check if password contains at least one digit
    password_has_digit = any(char.isdigit() for char in password)

    # Check if password contains at least one special character
    password_special_characters = "!@#$%^&*()_+[]{}|;:,.<>?/"
    has_special_character = any(
        char in password_special_characters for char in password)

    # Check if password contains both uppercase and lowercase letters
    password_has_uppercase = any(char.isupper() for char in password)
    password_has_lowercase = any(char.islower() for char in password)

    # Check if all conditions are met
    return password_has_digit and has_special_character and password_has_uppercase and password_has_lowercase


def main():
    try:
        password = input("Input your password: ")

        if Is_password_valid(password):
            print("Password is valid.")
        else:
            print("Password is invalid.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
