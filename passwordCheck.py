from sys import exit

from string import ascii_uppercase, ascii_lowercase, digits

def contains(required_chars, s):
    return any(c in required_chars for c in s)

def contains_upper(s):
    return contains(ascii_uppercase, s)

def contains_lower(s):
    return contains(ascii_lowercase, s)

def contains_digit(s):
    return contains(digits, s)

def contains_special(s):
    return contains(r"""!@$%^&*()_-+={}[]|\,.></?~`"':;""", s)

def long_enough(s):
    return len(s) >= 8

def check_len(input):
    if len(input) >= 8:
        return True
    else:
        return False

def validate_password(password):
    VALIDATIONS = (
        (contains_upper, 'Password needs at least one upper-case character.'),
        (contains_lower, 'Password needs at least one lower-case character.'),
        (contains_digit, 'Password needs at least one number.'),
        (contains_special, 'Password needs at least one special character.'),
        (long_enough, 'Password needs to be at least 8 characters in length.'),
    )
    failures = [
        failMsg for validator, msg in VALIDATIONS if not validator(password)
    ]
    if not failures:
        return True
    else:
        print("Invalid password! Review below and change your password accordingly!\n")
        for failMsg in failures:
            return failMsg + msg
            return False
            break

    if __name__ == '__main__':
        while True:
            password = validate_password(password)
            if validate_password(password):
                msg = ("Password meets all requirements and may be used.\n")
                return msg
                break

