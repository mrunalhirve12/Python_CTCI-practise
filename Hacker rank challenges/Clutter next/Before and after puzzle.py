from collections import defaultdict


def fuc(list):
    dict = defaultdict()
    res = ""
    l = []
    for sent in list:
        v = sent.split(' ', 1)[0]
        if v in dict.keys():
            dict[v].append(sent.split(' ',1)[1])
        else:
            dict[v] = [sent.split(' ',1)[1]]
    for sent in list:
        wlist = sent.split()
        if wlist[-1] in dict.keys():
            for val in dict[wlist[-1]]:
                res = sent + " "+ val
                l.append(res)
    return l

list = [
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
print(fuc(list))

