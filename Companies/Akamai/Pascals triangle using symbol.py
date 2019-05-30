"""
def printTriangle(num):
    c = "*"
    for i in range(num + 1):
        print(c * i)

print(printTriangle(4))
"""

def printTriangles(num):
    c = "*"
    for i in range(num ):
        st = ""
        for j in range(i+1):
            st += c
        print(st)

print(printTriangles(4))