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
def check(word):
    flag = True
    while flag:
        # A password must have at least 20 characters.
        if len(word) < 13:
            break
        # A password must contain an upper case letter.
        if flag:
            count_upper = 0
            for letter in word:
                if letter.isupper():
                    count_upper += 1
                    continue
            if count_upper < 1:
                break
        # A password must contain a lower case letter.
        if flag:
            count_lower = 0
            for letter in word:
                if letter.islower():
                    count_lower += 1
                    continue
            if count_lower < 1:
                break
        # A password must contain a special character.
        if flag:
            count_special_character = 0
            for letter in word:
                special_characters = '_@$^#5%'
                if letter in special_characters:
                    count_special_character += 1
                    continue
            if count_special_character < 1:
                break
        # A password must contain a number.
        if flag:
            count_number = 0
            for letter in word:
                if letter.isdigit():
                    count_number += 1
                    continue
            if count_number < 1:
                break

        return "Valid Password"
    return "Invalid Password"


print(check('R@m@_f0rtu9e$'))
print(check('Rama_fortune$'))
print(check('Rama#fortu9e'))
print(check('HdF^#dd258fa#nvnia7%6'))
print(check('hdf^#dd258fa#nvnia7%6'))
print(check('HDF^#DD258FA#NVNIA7%6'))
print(check('HdF^#dd258fa%6'))
