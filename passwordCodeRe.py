f"""
1) Write a method to check whether a given string is a valid password. Return true if it is valid and false otherwise.
Password rules:
A password must have at least 13 characters.
A password must contain an upper case letter.
A password must contain a lower case letter.
A password must contain a special character.
A password must contain a number.

§  Candidates will have the option of using a whiteboard
§  Candidates are not required to use any particular language
§  Candidates may also use pseudocode
"""
import re


def is_valid_password(password):
    # Check length
    if len(password) < 13:
        return False

    # Check for upper case letter
    if not re.search("[A-Z]", password):
        return False

    # Check for lower case letter
    if not re.search("[a-z]", password):
        return False

    # Check for special character
    if not re.search("[\W_]", password):
        return False

    # Check for number
    if not re.search("[\d]", password):
        return False

    return True


print(is_valid_password('R@m@_f0rtu9e$'))
print(is_valid_password('Rama_fortune$'))
print(is_valid_password('Rama#fortu9e'))
print(is_valid_password('HdF^#dd258fa#nvnia7%6'))
print(is_valid_password('hdf^#dd258fa#nvnia7%6'))
print(is_valid_password('HDF^#DD258FA#NVNIA7%6'))
print(is_valid_password('HdF^#dd258fa%6'))
