def generate_phrases(phrases):
    dict = {}
    res = []
    for i in range(len(phrases)):
        arr = phrases[i].split()
        s = ' '.join(arr[1:])
        if arr[0] in dict:
            dict[arr[0]].append(s)
        else:
            dict[arr[0]] = [s]
    for i in range(len(phrases)):
        arr = phrases[i].split()
        s = ' '.join(arr)
        if arr[len(arr)-1] in dict:
            for value in dict[arr[len(arr)-1]]:
                temp = s + " "+value
                res.append(temp)
    return res

phrases = [
    'mission statement',
    'a quick bite to eat',
    'a chip off the old block',
    'chocolate bar',
    'mission impossible',
    'a man on a mission',
    'block party',
    'eat my words',
    'bar of soap'
]
print(generate_phrases(phrases))