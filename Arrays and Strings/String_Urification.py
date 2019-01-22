# c++ solution - https://www.geeksforgeeks.org/urlify-given-string-replace-spaces/
# -------To understand step by step solution---------------------------------


# Time and space complexity O(n)
Max = 1000


def string_urify(str, str_len):

    # using for loop
    str_r = str.rstrip(' ')
    for i in range(len(str_r)):
        str1 = str_r.replace(' ', '%20')
    print(str1)

    # using direct
    str = str[:str_len].replace(' ', '%20')
    print(str)


string_urify('How are you ', 11)
