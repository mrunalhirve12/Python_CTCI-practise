import sys

def minimumDistance(numRows, numColumns, area):
    def isValid(area, x, y):
        return 0 <= x < len(area) and 0 <= y < len(area[0]) and (area[x][y] == 1 or area[x][y] == 9)

    def updateMinDist(minDistanceTillNow, minDistFound):
        if minDistanceTillNow == -1:
            return minDistFound

        if minDistFound == -1:
            return minDistanceTillNow

        if minDistanceTillNow > minDistFound:
            return minDistFound

        return minDistanceTillNow

    def minDist(area, currx, curry, steps):
        if area[currx][curry] == -1:
            return -1

        if area[currx][curry] == 9:
            return steps

        area[currx][curry] = -1

        curr_minDist = -1

        if isValid(area, currx + 1, curry):
            curr_minDist = updateMinDist(curr_minDist, minDist(area, currx + 1, curry, steps + 1))

        if isValid(area, currx - 1, curry):
            curr_minDist = updateMinDist(curr_minDist, minDist(area, currx - 1, curry, steps + 1))

        if isValid(area, currx, curry + 1):
            curr_minDist = updateMinDist(curr_minDist, minDist(area, currx, curry + 1, steps + 1))

        if isValid(area, currx, curry - 1):
            curr_minDist = updateMinDist(curr_minDist, minDist(area, currx, curry - 1, steps + 1))

        #area[currx][curry] = -1
        return curr_minDist

    if numRows < 1 or numColumns > 1000 or numColumns < 1:
        return -1
    min_dist = minDist(area, 0, 0, 0)
    return min_dist


area = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]
print(minimumDistance(5, 4, area))
