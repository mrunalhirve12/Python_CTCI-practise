import sys
from collections import Counter


def smallest_set(start, end, c):
    d = {}
    d[start - 1] = []
    for i in range(start, end + 1):
        d[i] = []
        prev_len = len(d[i - 1])
        new_lists = c[i] - prev_len
        if new_lists > 0:
            d[i] = [1] * new_lists
        if prev_len > 0:
            num_appends = min(prev_len, new_lists + prev_len)
            d[i - 1].sort()
            d[i] += [x + 1 for x in d[i - 1][:num_appends]]
            d[i - 1] = d[i - 1][num_appends:]
    ans = d[end][0]
    for i in range(start, end + 1):
        if len(d[i]) > 0:
            ans = min(ans, min(d[i]))
            if ans == 1:
                return 1

    return ans

def find_lowest_range(l, n):
    c = Counter(l)
    i = 0
    mini = n
    while i < len(l):
        end = i
        while end < n and (l[i] == l[end] or (abs(l[end] - l[end - 1]) == 1)):
            end += 1
        end -= 1
        if end == i:
            return 1
        mini = min(mini, smallest_set(l[i], l[end], c))
        if mini == 1:
            return 1
        i = end + 1
    return mini


t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    if l[0] == 0:
        print(0)
        continue
    n = l[0]
    l = sorted(l[1:])
    print(find_lowest_range(l, n))

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def smallest_set(start, end, c):
    d = {}
    d[start - 1] = []
    for i in range(start, end + 1):
        d[i] = []
        prev_len = len(d[i-1])
        new_lists = c[i] - prev_len
        if new_lists > 0:
            d[i] = [1]*new_lists
        if prev_len > 0:
            num_appends = min(prev_len, new_lists + prev_len)
            d[i-1].sort()
            d[i] += [x+1 for x in d[i-1][:num_appends]]
            d[i-1] = d[i-1][num_appends:]
    ans = d[end][0]
    for i in range(start, end + 1):
        if len(d[i]) > 0:
            ans = min(ans, min(d[i]))
            if ans == 1:
                return 1
            
    return ans

def find_lowest_range(l, n):
    c = Counter(l)
    i = 0
    mini = n
    while i < len(l):
        end = i
        while end < n and (l[i] == l[end] or (l[end] - l[end - 1]) <= 1):
            end += 1
        end -= 1
        if end == i:
            return 1
        mini = min(mini, smallest_set(l[i], l[end], c))
        if mini == 1:
            return 1
        i = end + 1
    return mini

t = int(raw_input())
for _ in range(t):
    l = list(map(int, raw_input().split()))
    if l[0] == 0:
        print(0)
        continue
    n = l[0]    
    l = sorted(l[1:])
    print(find_lowest_range(l, n))

"""