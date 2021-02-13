# -*- coding: utf-8 -*- 
from typing import *


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         length = len(nums)
#         res = [1] * length
#         left, right = 1, 1
#         for i in range(length):
#             res[i] *= left
#             left *= nums[i]
#
#             res[length-1-i] *= right
#             right *= nums[length-i-1]
#         return res

# 搜索二维矩阵 II
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         def helper(nums):
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if nums[mid] == target:
#                     return True
#                 elif nums[mid] > target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return False
#
#         for nums in matrix:
#             if helper(nums):
#                 return True
#         return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        inf = float("inf")
        twos, ones = inf, inf
        for i, n in enumerate(nums):
            if n < twos:
                twos = n
            elif twos < n < ones:
                ones = n
            else:
                return True
        return False


s = Solution()
print(s.increasingTriplet([1,2,3,4,5]))
