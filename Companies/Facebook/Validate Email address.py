import re


def isValidEmail(email):
    if len(email) > 7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email) is not None:
            return True
        return False


if isValidEmail("my.email@gmail.com"):
    print("This is a valid email address")
else:
    print("This is not a valid email address")