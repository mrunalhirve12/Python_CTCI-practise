import re
import sys

def solution(S):
    # write your code in Python 3.6
    if len(S) < 1:
        return 0
    if len(S) == 1:
        if "." in S or "?" in S or "!" in S:
            return 0
    max = -sys.maxsize
    sentences = re.split('\\.|\\!|\\?', S)
    for sentence in sentences:
        words = sentence.split()
        #print(words)
        count_words = len(words)
        if count_words > max:
            max = count_words
    #print(max)
    return max

#print(solution("We test coders. Give us a try?"))
#print(solution("F"))
#print(solution("."))
print(solution(""))