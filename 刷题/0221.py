# -*- coding: utf-8 -*- 
from typing import *


# 最后一块石头的重量
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         import heapq
#         stones = [-i  for i in stones]
#         heapq.heapify(stones)
#         while len(stones) >1:
#             f = heapq.heappop(stones)
#             s = heapq.heappop(stones)
#             heapq.heappush(stones, f-s)
#         return -stones[0] if stones[0] else 0

# 最小差值 II
# class Solution:
#     def smallestRangeII(self, A: List[int], K: int) -> int:
#         A.sort()
#         mi, ma = A[0], A[-1]
#         res = ma - mi
#         for i in range(len(A) - 1):
#             a, b = A[i], A[i + 1]
#             res = min(res, max(ma - K, a + K) - min(mi + K, b - K))
#         return res

#  回文子串
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#
#         res = 0
#         length = len(s)
#         dp = [[False] * length for _ in range(length)]
#         for i in range(len(s)):
#             for j in range(i + 1):
#                 if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
#                     dp[j][i] = True
#                     res += 1
#         return res

# 按摩师
# class Solution:
#     def massage(self, nums: List[int]) -> int:
#         a, b = 0, 0
#         for n in nums:
#             b, a = max(a + n, b), b
#         return b
