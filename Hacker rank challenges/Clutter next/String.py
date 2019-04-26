def string(words):
    s = ""
    n = len(words)
    s = words[n-1] + " " + words[n-2]
    return s

print(string("bat"))