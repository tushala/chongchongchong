# -*- coding: utf-8 -*-
# 0223.py 欠
from typing import *


# 礼物的最大价值

# class Solution:
#     def maxValue(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[0] * (1 + n) for _ in range(1 + m)]
#         for i in range(1, m+1):
#             for j in range(1, n+1):
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
#         return dp[-1][-1]

# 矩阵中的路径


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         m, n = len(board), len(board[0])
#
#         def dfs(i, j, word):
#             if not word:
#                 return True
#             if i < 0 or i >= m or j < 0 or j >= n:
#                 return False
#
#             if board[i][j] == word[0]:
#                 board[i][j] = "#"
#                 for x, y in dir:
#                     nx, ny = i + x, j + y
#                     r = dfs(nx, ny, word[1:])
#                     if r:
#                         return True
#                 board[i][j] = word[0]
#             return False
#
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] == word[0]:
#                     # board_ = board[:]
#                     # print(board_)
#                     res = dfs(i, j, word)
#                     if res:
#                         return True
#         return False


s = Solution()
print(s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
print(s.exist(board=[["a", "b"], ["c", "d"]], word="abcd"))
print(s.exist(board=[["a"]], word="a"))
print(s.exist([["a", "a"]], 'aaa'))
print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], 'AAB'))  # todo
