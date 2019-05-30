def reverse(words):
    words = words.split()
    i = 0
    j = len(words) - 1
    while i < j:
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1
    return " ".join(words)


print(reverse("I am Mrunal"))


def reverseLetters(words):
    words = words.split()
    res = []
    for i in range(len(words)):
        word = list(words[i])
        i = 0
        j = len(word)-1
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        word = "".join(word)
        res.append(word)
    return " ".join(res)


print(reverseLetters("I am Mrunal"))


def reverseLettersWords(words):
    words = words.split()
    res = []
    for i in range(len(words)-1, -1, -1):
        word = list(words[i])
        i = 0
        j = len(word)-1
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        word = "".join(word)
        res.append(word)
    return " ".join(res)


print(reverseLettersWords("I am Mrunal"))