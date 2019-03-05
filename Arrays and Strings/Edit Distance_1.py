def isEditDistanceOne(s1, s2):
    m = len(s1)
    n = len(s2)
    if abs(m - n) > 1:  # pale le
        return False
    counter = 0
    i = 0
    j = 0
    while i < m & j < n:  # counters
        if s1[i] != s2[j]:
            if counter == 1:  # if diff more than 1
                return False
            if m > n:  # pale ale
                i += 1
            elif n > m:  # ale pale
                j += 1
            else:
                i += 1
                j += 1
            counter += 1  # pale le
        else:
            i += 1
            j += 1
    if i < m or j < n:  # pale pa
        counter += 1
    return counter == 1

s1 = "pale"
s2 = "alee"
if isEditDistanceOne(s1, s2):
    print("Yes")
else:
    print("No")







