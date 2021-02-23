# -*- coding: utf-8 -*- 
from typing import *

# 括号

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         if n < 0: return []
#         if n == 0: return ['']
#
#         res = set()
#         for s in self.generateParenthesis(n - 1):
#             for i in range(2 * n - 1):
#                 if s[:i] + '()' + s[i:] in res:
#                     continue
#                 res.add(s[:i] + '()' + s[i:])
#
#         return list(res)

# 最大子序和
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = float("-inf")
#         cur = 0
#         for n in nums:
#             cur = max(cur + n, n)
#             res = max(res, cur)
#         return res


# 单词接龙


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
#         chs = [chr(97 + i) for i in range(26)]
#         res = 1
#         length = len(beginWord)
#         rec = set(wordList)
#         curwords = {beginWord}
#         while curwords:
#             nxtwords = set()
#             for cw in curwords:
#                 for i in range(length):
#                     for ch in chs:
#                         new_words = cw[:i] + ch + cw[i + 1:]
#                         if new_words == endWord:
#                             return res + 1
#                         if new_words in rec:
#                             nxtwords.add(new_words)
#                             rec.remove(new_words)
#             curwords = nxtwords
#             res += 1
#         return 0

# 岛屿数量
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         res = 0
#         m, n = len(grid), len(grid[0])
#
#         def dfs(i, j):
#             if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
#                 return
#             grid[i][j] = "0"
#             for x, y in dir:
#                 ni = i + x
#                 nj = j + y
#                 dfs(ni, nj)
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     res += 1
#
#         return res

# 课程表
from collections import defaultdict

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites):
#         n = [0] * numCourses
#         d = defaultdict(list)
#         for i, o in prerequisites:
#             n[i] += 1
#             d[o].append(i)
#         queue = []
#         for i in range(numCourses):
#             if not n[i]:
#                 queue.append(i)
#
#         while queue:
#             c = queue.pop(0)
#             numCourses -= 1
#             for i in d[c]:
#                 n[i] -= 1
#                 if not n[i]:
#                     queue.append(i)
#         return numCourses == 0

# 课程表 II

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         n = [0] * numCourses
#         d = defaultdict(list)
#         for e, s in prerequisites:
#             n[e] += 1
#             d[s].append(e)
#
#         queue = []
#         for i in range(numCourses):
#             if not n[i]:
#                 queue.append(i)
#
#         res = []
#         while queue:
#             c = queue.pop(0)
#             numCourses -= 1
#             res.append(c)
#             for i in d[c]:
#                 n[i] -= 1
#                 if not n[i]:
#                     queue.append(i)
#
#         return res if not numCourses else []
