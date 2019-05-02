import re


def isValidIP(email):
    if len(email) > 7:
        if re.match("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", email) is not None:
            return True
        return False


if isValidIP("999.999.999.999"):
    print("This is a valid IP address")
else:
    print("This is not a valid IP address")
