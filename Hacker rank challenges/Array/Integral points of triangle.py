import math
import sys


def gcd(a,b):
    if b == 0:
        return int(a)
    return gcd(b, a%b)

def getBoundaryCount(p, q):
    if p[0] == q[0]:
        return (int(p[0]) ,int(abs(p[1]-q[1])-1))
    if p[1] == q[1]:
        return  (int((abs(p[0] - q[0])-1)), int(q[1]))

    return (gcd(abs(p[0]-q[0]), abs(p[1]-q[1]))-1, 0)

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def mindist(boundaryPoints, p ,q ,r):
    mins = sys.maxsize
    for i in range(len(boundaryPoints)):
        sum = distance(i,p) + distance(i,q) + distance(i,r)
        if (sum < mins):
            mins = sum

def  find_min_point(x1, y1, x2, y2, x3, y3):

    # 3 extra integer points for the vertices
    p = (x1, y1)
    q = (x2, y2)
    r = (x3, y3)
    boundaryPoints = []
    boundaryPoints.append(getBoundaryCount(p, q))
    boundaryPoints.append(getBoundaryCount(p, r))
    boundaryPoints.append(getBoundaryCount(q, r))

    mindist(boundaryPoints, p, q, r)


find_min_point(0.0, 0.0, 1.0, 0.0, 1.0, 1.0)