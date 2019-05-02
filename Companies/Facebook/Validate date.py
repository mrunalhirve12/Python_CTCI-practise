import re


def isValidDate(email):
    if len(email) > 7:
        if re.match("^\d{1,2}\/\d{1,2}\/\d{4}$", email) is not None:
            return True
        return False


if isValidDate("4/1/2001"):
    print("This is a valid date")
else:
    print("This is not a valid date")