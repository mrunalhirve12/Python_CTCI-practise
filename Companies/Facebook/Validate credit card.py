import re


def isValidCreditCard(email):
    if len(email) > 7:
        if re.match("^\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}$", email) is not None:
            return True
        return False


if isValidCreditCard("5555555555554444"):
    print("This is a valid credit card")
else:
    print("This is not a valid credit card")