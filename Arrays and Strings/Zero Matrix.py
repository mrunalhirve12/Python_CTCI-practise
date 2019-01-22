# Python3 Code For A Boolean Matrix Question
# pg 215
def zeroMatrix(mat):
    row = len(mat) * [False]
    col = len(mat[0]) * [False]

    # check for first rows and columns if 0
    for i in range(len(row)):
        for j in range(len(col)):
            if mat[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(len(row)):
        if row[i]:
            for j in range(len(col)):
                mat[i][j] = 0

    for i in range(len(col)):
        if col[i]:
            for j in range(len(row)):
                mat[j][i] = 0
    print(mat)


mat = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]

zeroMatrix(mat)
