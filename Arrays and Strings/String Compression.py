# http://davidbpython.com/advanced_python/slides/exercise_solution-10-3.html
def string_compression(string):
    counter = 0
    compressed = []

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i-1] + str(counter))
            counter = 0
        counter += 1

    compressed.append(string[-1] + str(counter))
    newstr = ''.join(compressed)
    if len(newstr) < len(string):
        print(newstr)
    else:
        print(string)


string_compression("aabbb")
string_compression("abcdef")
