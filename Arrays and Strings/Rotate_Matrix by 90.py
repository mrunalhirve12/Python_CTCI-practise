# http://davidbpython.com/advanced_python/slides/exercise_solution-10-3.html
def rotate_matrix(matrix):
    n = len(matrix)
    if n == 0 | n != len(matrix[0]):
        return False
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            offset = i-first

            # save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    print(matrix)


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

rotate_matrix(matrix)


