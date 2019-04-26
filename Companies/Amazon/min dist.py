
def removeObstacles(numRows, numColumns, lot):
    res = 0
    tc = [[0 for x in range(numColumns)] for x in range(numRows)]

    tc[0][0] = lot[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, numRows):
        tc[i][0] = tc[i - 1][0] + lot[i][0]

    # Initialize first row of tc array
    for j in range(1, numColumns):
        tc[0][j] = tc[0][j - 1] + lot[0][j]

        # Construct rest of the tc array
    for i in range(1, numRows):
        for j in range(1, numColumns):
                tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j],
                               tc[i][j - 1]) + lot[i][j]
                if lot[i][j] == 9:
                    res = tc[i][j]
    return res

mat = [[1,0,0],[1,0,0],[1,9,1]]
print(removeObstacles(3,3,mat))







