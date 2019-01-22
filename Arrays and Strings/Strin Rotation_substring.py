def isSubString(s1, s2):
    n = len(s1)
    n2 = len(s2)
    s = ''
    if n == n2 and n > 0:
        s = s1 + s2
        print(s)
        return isSubString(s, s2)
    return False


isSubString("zeroflag", "oflagzer")
