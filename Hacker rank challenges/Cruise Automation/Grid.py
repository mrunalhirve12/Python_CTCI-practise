import math
import sys

import numpy as np

"""
def countMax(upRight):
    # Write your code here
    #a = math.floor(float('inf'))
    max = -sys.maxsize - 1
    max_val = []
    mat = [[0 for x in range(50)] for y in range(50)]
    for i in upRight:
            m = i.split()[0]
            n = i.split()[1]
            for i in range(1, int(m)):
                for j in range(1, int(n)):
                    mat[i][j] += 1
    max = mat[1][1]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if max == mat[i][j]:
                max_val.append(mat[i][j])
    return len(max_val)
"""

def countMax(upRight):
    # Write your code here
    #a = math.floor(float('inf'))
    max = -sys.maxsize - 1
    max_val = []
    mat_f = [[0 for x in range(10)] for y in range(10)]
    # print(mat_f)
    for i in upRight:
            m = i.split()[0]
            n = i.split()[1]
            mat_i = [[0 for x in range(int(n))] for y in range(int(m))]
            # print(mat_i)
            for i in range(int(m)):
                for j in range(int(n)):
                    mat_i[i][j] += 1
            print(mat_i)
            res = add_mat(mat_f, mat_i)
    print(res)
    return maxx(res)

def add_mat(mat_f, mat_i):
    row = min(len(mat_i), len(mat_f))
    col = min(len(mat_i[0]), len(mat_f[0]))
    for i in range(row):
        for j in range(col):
            mat_f[i][j] = mat_f[i][j] + mat_i[i][j]
    return mat_f

def maxx(res):
    count = 0
    max_elem = res[0][0]
    for i in range(len(res)):
        for j in range(len(res[0])):
            if res[i][j] == max_elem:
                count +=1
    return count


print(countMax(["2 3", "3 7", "4 1"]))