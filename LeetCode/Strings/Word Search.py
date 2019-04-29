"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, y, x, visit):
            # if length of word is 0; return True
            if len(word) == 0:
                return True
            # if len of word is 1 and word in at the given location then return True
            elif len(word) == 1:
                return board[y][x] == word
            else:
                # if the word[0] is at board[y][x] location; then keep processing
                if board[y][x] == word[0]:
                    # mark it as visited
                    visit[y][x] = True
                    # chk if visited and if valid indexed and keep iterating
                    if y > 0 and not visit[y - 1][x]:
                        if dfs(board, word[1:], y - 1, x, visit):
                            return True
                    if y < height - 1 and not visit[y + 1][x]:
                        if dfs(board, word[1:], y + 1, x, visit):
                            return True
                    if x > 0 and not visit[y][x - 1]:
                        if dfs(board, word[1:], y, x - 1, visit):
                            return True
                    if x < width - 1 and not visit[y][x + 1]:
                        if dfs(board, word[1:], y, x + 1, visit):
                            return True
                    visit[y][x] = False
                    return False
                # else return False if word not there
                else:
                    return False

        height = len(board)
        width = len(board[0])
        # take a visited matrix mark it with False
        visit = [[False] * width for _ in range(height)]
        #if height == 1 and width == 0:
            #return len(word) == 0
        # iterate in dfs order; pass word index and visited matrix
        for i in range(height):
            for j in range(width):
                if dfs(board, word, i, j, visit):
                    return True
        return False


s = Solution()
board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
print(s.exist(board, "ABCCED"))