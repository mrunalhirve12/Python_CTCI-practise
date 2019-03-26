class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #finding the len of rows and columns
        rowLen = len(matrix)
        colLen = len(matrix[0])

        #creating a array for holding rows and columns
        row = [False]*rowLen
        col = [False]*colLen

        #to find any row or column having val 0
        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        #check in rows and set row to 0
        for i in range(len(row)):
            if row[i] == True:
                    for cols in range(colLen):
                        matrix[i][cols] = 0

        # check in cols and set col to 0
        for i in range(len(col)):
            if col[i] == True:
                    for rows in range(rowLen):
                        matrix[rows][i] = 0

        return matrix
s = Solution
s.setZeroes(s,[[1,1,1],[1,0,1],[1,1,1]])