# -*- coding: utf-8 -*- 
from typing import *


# 1423
# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         length = len(cardPoints)
#         prelist = [0] * (length + 1)
#         for i in range(length):
#             prelist[i + 1] = cardPoints[i] + prelist[i]
#         s = sum(cardPoints)
#         t = length - k
#         smallestksum = min([prelist[i + t] - prelist[i] for i in range(length - t + 1)])
#         return s - smallestksum


# 实现 Trie (前缀树)
# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}
#
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         s = self.trie
#         for i in word:
#             s[i] = s.get(i, {})
#             # if i not in s:
#             #     s[i] = {}
#             s = s[i]
#
#         s['exist'] = True
#
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         s = self.trie
#         for w in word:
#             if w not in s:
#                 return False
#             s = s[w]
#         return s.get("exist", False)
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         s = self.trie
#         for i in prefix:
#             if i in s:
#                 s = s[i]
#             else:
#                 return False
#         return True


# 有效的字母异位词
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return  Counter(s) == Counter(t)

# 字符串中的第一个唯一字符
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         c = Counter(s)
#         for n, _s in enumerate(s):
#             if c[_s] == 1:
#                 return n
#
#         return -1

# 反转字符串
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i, j = 0, len(s) - 1
#         while i < j:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1

# 单词搜索 II
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m, n = len(board), len(board[0])
#         root = {}
#         for w in words:
#             p = root
#             for c in w:
#                 if c not in p:
#                     p[c] = {}
#                 p = p[c]
#             p['finish'] = w
#
#         def dfs(start, p):
#             i, j = start
#             c = board[i][j]
#             last = p[c].pop('finish', False)
#             if last:
#                 res.append(last)
#             board[i][j] = "#"
#
#             for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 ni, nj = i + x, j + y
#                 if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in p[c]:
#                     dfs((ni, nj), p[c])
#             board[i][j] = c
#
#         res = []
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] in root:
#                     dfs((i, j), root)
#         return res
