import random
"""
def rand5():
    return random.randint(0,4)
    pass


def rand7():
    val = [[1,2,3,4,5],[6,7,1,2,3],[4,5,6,7,1],[2,3,4,5,6],[7,0,0,0,0]]
    result = 0
    while result == 0:
        i = rand5()
        j = rand5()
        result = val[i-1][j-1]
    return result

print(rand7())
"""

def rand3():
    return random.randint(0,2)
    pass


def rand9():
    val = [[1,2,3],[4,5,7],[7,8,9]]
    result = 0
    while result == 0:
        i = rand3()
        j = rand3()
        result = val[i-1][j-1]
    return result

print(rand9())
print(rand9())
print(rand9())
print(rand9())
print(rand9())
print(rand9())
print(rand9())