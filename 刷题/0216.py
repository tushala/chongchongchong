# -*- coding: utf-8 -*-
from typing import *

# 最大数
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         nums = sorted(nums, key=lambda x: x / int('9' * len(str(x))), reverse=True)
#         return str(int("".join([str(i) for i in nums])))
# 寻找峰值
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         def search(l, r):
#             if l == r:
#                 return l
#             mid = (l + r) // 2
#             if nums[mid] > nums[mid + 1]:
#                 return search(l, mid)
#             return search(mid + 1, r)
#
#         return search(0, len(nums) - 1)


# 寻找重复数
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         left, right = 1, n
#         while left <= right:
#             mid = (left + right) // 2
#             count = sum(i <= mid for i in nums)
#             if count <= mid:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left
