import sys
import operator

def unique_file(k):
    input_file = open('2.txt', 'r')
    file_contents = input_file.read()
    input_file.close()
    maxe = 0
    dict= {}
    word_list = file_contents.split()
    c1 = c2 = c3 = 0
    third = first = second = -sys.maxsize
    for word in word_list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    for i in range(k):
        word = max(dict.iteritems(), key=operator.itemgetter(1))[0]




"""
    for word in dict:
        if dict[word] > c1:
            third, c3 = second, c2
            second, c2 = first, c1
            first, c1 = word, dict[word]

        elif dict[word] > c2:
            third, c3 = second, c2
            second, c2 = word, dict[word]

        elif dict[word] > c3:
            third, c3 = word, dict[word]

    return first, second, third
"""

print(unique_file())
