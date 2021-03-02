# -*- coding: utf-8 -*- 
from typing import *

# 1771

# class Solution:
#     def longestPalindrome(self, word1: str, word2: str) -> int:
#         res = 0
#         s = word1 + word2
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 1
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                     if i < len(word1) <= j:
#                         res = max(res, dp[i][j])
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])


# 516

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         res = 1
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 1
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#                 else:
#                     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
#                 res = max(res, dp[i][j])
#         return res

# 面试题 08.12.
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         line_ = '.' * n
#
#         def conflict(state, num):
#             n = len(state)
#             for i in range(n):
#                 if abs(state[i] - num) in (0, n - i):  # 下一个皇后与当前皇后在同一列或位于同一对角线
#                     return True
#             return False
#
#         def dfs(state, n):
#             for i in range(n):
#                 if not conflict(state, i):
#                     if len(state) == n - 1:
#                         yield (i,)
#                     else:
#                         for r in dfs(state + (i,), n):
#                             yield (i,) + r
#
#         def pprint(state):
#
#             ans = []
#             for s in state:
#                 line = line_[:s] + 'Q' + line_[s + 1:]
#                 ans.append(line)
#             res.append(ans)
#
#         for r in dfs((), n):
#             pprint(r)
#         return res

# 面试题 16.26.
# class Solution:
#     def calculate(self, s: str) -> int:
#         s = s.strip()
#         num = ''
#         res = []
#         fh = '+'
#         for n, i in enumerate(s):
#             if not i:
#                 continue
#             if i in ['+', '-', '*', '/'] or n == len(s) - 1:
#                 if n == len(s) - 1:
#                     num += i
#                 num = int(num)
#                 if fh == '*' or fh == "/":
#                     res.append(int(eval(f"{res.pop()}{fh}{num}")))
#                 else:
#                     res.append((1 if fh == '+' else -1) * num)
#                 num = ""
#                 fh = i
#             else:
#                 num += i
#
#         return sum(res)

# 子集 II
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         def subset(nums, index):
#             if index == 0:
#                 return [[]]
#             tmp = subset(nums, index - 1)
#             ans = tmp[:]
#             for i in tmp:
#                 if i + [nums[index - 1]] not in ans:
#                     ans.append(i + [nums[index - 1]])
#             return ans
#
#         return subset(nums, len(nums))

# 剑指 Offer 04.
# class Solution:
#     def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix:
#             return False
#
#         m, n = len(matrix), len(matrix[0])
#         row, col = 0, n - 1
#
#         while row < m and col >= 0:
#             if matrix[row][col] < target:
#                 row += 1
#             elif matrix[row][col] > target:
#                 col -= 1
#             else:
#                 return True
#         return False


# 剑指 Offer 59 - I


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums:
#             return []
#         stack = []
#         res = [0] * (len(nums) - k + 1)
#         for i, n in enumerate(nums):
#             while stack and i - stack[0] >= k:
#                 stack.pop(0)
#             while stack and n > nums[stack[-1]]:
#                 stack.pop()
#             stack.append(i)
#             if i >= k - 1:
#                 res[i - k + 1] = nums[stack[0]]
#         return res
