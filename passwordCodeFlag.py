'''
1) Write a method to check whether a given string is a valid password. Return true if it is valid and false otherwise.
Password rules:
A password must have at least 20 characters.
A password must contain an upper case letter.
A password must contain a lower case letter.
A password must contain a special character.
A password must contain a number.

§  Candidates will have the option of using a whiteboard
§  Candidates are not required to use any particular language
§  Candidates may also use pseudocode
'''
import re
password = 'HdF^#dd258fa#nvnia7%6'
flag = 0
while True:
    if len(password) <= 20:
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[~`_@!#$%^&*()+?><]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password ")

