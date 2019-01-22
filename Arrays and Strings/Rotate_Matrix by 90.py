import unittest


# http://davidbpython.com/advanced_python/slides/exercise_solution-10-3.html
def rotate_matrix(matrix):
    n = len(matrix)
    print(n)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        print(first)
        print(last)
        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
        return matrix


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


class Test(unittest.TestCase):
    """Test Cases"""
    data = [
        ([
             [1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [21, 16, 11, 6, 1],
             [22, 17, 12, 7, 2],
             [23, 18, 13, 8, 3],
             [24, 19, 14, 9, 4],
             [25, 20, 15, 10, 5]
         ])
    ]


def test_rotate_matrix(self):
    for [matrix, result] in self.data:
        actual = rotate_matrix(matrix)
        if self.assertEqual(actual, result):
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    unittest.main()
