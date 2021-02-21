# -*- coding: utf-8 -*- 
from typing import *


# 435. 无重叠区间

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0
#         intervals = sorted(intervals, key=lambda x: x[1])
#         res = 0
#         s, e = intervals[0]
#         for _s, _e in intervals[1:]:
#             if _s < e:
#                 res += 1
#             else:
#                 s, e = _s, _e
#         return res


# 字母大小写全排列
# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         S = S.lower()
#         def helper(S):
#             if not len(S):
#                 return ['']
#             s, _S = S[0], S[1:]
#             _res = helper(_S)
#             if s.isdigit():
#                 res = [s+i for i in _res]
#             else:
#                 res = [s + i for i in _res] + [s.upper() + i for i in _res]
#             return res
#         return helper(S)

# 打家劫舍


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) < 2:
#             return max(nums)
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#         return dp[-1]

# 完全平方数
# class Solution:
#     def numSquares(self, n: int) -> int:
#         def issq(n):
#             return n == int(n ** 0.5) ** 2
#
#         dp = [n] * (n + 1)
#         dp[0] = 0
#         dp[1] = 1
#         s = {i ** 2 for i in range(1, int(n ** 0.5) + 1)}
#         for i in range(2, n + 1):
#             if i in s:
#                 dp[i] = 1
#                 continue
#             for j in s:
#                 dp[i] = min(dp[i], dp[i - j] + 1)
#         return dp[-1]

# 最长上升子序列


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
# length = len(nums)
# dp = [1] * length
# for i in range(1, length):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)

# return max(dp)
# from bisect import bisect_left
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         """
#         读题：寻找最长严格递增子序列
#
#         思路：dp
#             1）状态定义：dp = 到达第i位时的最长子序列长度。
#
#         优化：维护一个结果列表，使用二分查找确定新的元素在结果列表中的位置。
#             1）比结果列表中的值小，替换结果列表中比该元素大的第一个下标元素。
#             2）比结果列表的值都大，则添加到已有元素的末尾。
#             3）结果列表的长度，即为已找到的最长严格递增子序列的长度。
#         """
#
#         if len(nums) <= 1:
#             return len(nums)
#         dp = []
#         for num in nums:
#             index = bisect_left(dp, num)
#             if index == len(dp):
#                 dp.append(num)
#             else:
#                 dp[index] = num
#         return len(dp)

# 最大连续1的个数 III
# class Solution:
#     def longestOnes(self, A: List[int], K: int) -> int:
#         n = len(A)
#         res = 0
#         left, right, zeros = 0, 0, 0
#         while right < n:
#             if A[right] == 0:
#                 zeros += 1
#                 if zeros > K:
#                     while A[left] == 1:
#                         left += 1
#                     left += 1
#                     zeros = K
#             res = max(res, right - left + 1)
#             right += 1
#         return res


