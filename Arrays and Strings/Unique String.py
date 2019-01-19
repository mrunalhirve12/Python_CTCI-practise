# Without using additional data structures
# using data structures
# Time Complexity : O(n2)

def naive_unique(s):
    # naive solution with O(n2) complexity
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                print("duplicates")
                return
    print("all unique")


naive_unique('vhgfhgfhf')
naive_unique('abc')


# ----Time complexity: O(n log n)--------------------------------------------------------------------

def uniques(s):
    # sorting first
    if len(s) == 1:
        print("all unique")
    if len(s) == 2:
        if (s[0] == s[1]):
            print("Duplicates")
        else:
            print("all unique")
        return
    s = sorted(s)
    for j in range(len(s) - 1):
        if (s[j] == s[j + 1]):
            print("Duplicates found")
            return
    print("Unique")


uniques('vhgfhgfhf')
uniques('abc')


# --Time Complexity: O(n),Using data structure-----------------------------------------------------------------------------
def uniques(s):
    uchar = set()
    for c in s:
        if c in uchar:
            return False
        uchar.add(s)
    return True
