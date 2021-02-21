# -*- coding: utf-8 -*- 
from typing import *


# 电话号码的字母组合
# 题目链接
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         key = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#         if not digits:
#             return []
#         def helper(digits):
#             if not digits:
#                 return ['']
#             d1, di = digits[0], digits[1:]
#             _res = helper(di)
#             res = []
#             for v in key[d1]:
#                 res.extend([v+i for i in _res])
#             return res
#         return helper(digits)


# 面试题 08.07. 无重复字符串的排列组合

# class Solution:
#     def permutation(self, S: str) -> List[str]:
# def helper(S):
#     if len(S) == 0:
#         return [""]
#     res = []
#     for i, s in enumerate(S):
#         es = S[:i] + S[i+1:]
#         _res = helper(es)
#         res.extend([s+r for r in _res])
#     return res
# return helper(S)
# import itertools
# res = itertools.permutations(S, len(S))
# return [''.join(item) for item in res]


# 零钱兑换

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float("inf")] * (amount + 1)
#         dp[0] = 0
#         for i in range(1, amount + 1):
#             dp[i] = min(dp[i - c] if i - c >= 0 else float("inf") for c in coins) + 1
#         return dp[-1] if dp[-1] != float("inf") else -1


# 矩阵中的最长递增路径


# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix:
#             return 0
#         dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         m, n = len(matrix), len(matrix[0])
#
#         @lru_cache(None)
#         def dfs(x, y):
#             ans = 1
#             for d in dir:
#                 nx, ny = x + d[0], y + d[1]
#                 if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
#                     ans = max(ans, dfs(nx, ny) + 1)
#             return ans
#
#         res = 0
#         for i in range(m):
#             for j in range(n):
#                 res = max(res, dfs(i, j))
#         return res
