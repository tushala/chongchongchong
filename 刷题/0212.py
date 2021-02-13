# -*- coding: utf-8 -*- 
from typing import *


# 打乱数组
# import random
#
#
# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.arry = nums
#         self.ori = nums[:]
#
#     def reset(self) -> List[int]:
#         """
#         Resets the array to its original configuration and return it.
#         """
#         self.arry = self.ori
#         self.ori = self.ori[:]
#         return self.arry
#
#     def shuffle(self) -> List[int]:
#         """
#         Returns a random shuffling of the array.
#         """
#         for i in range(len(self.arry)):
#             swp_idx = random.randrange(i, len(self.arry))
#             self.arry[swp_idx], self.arry[i] = self.arry[i], self.arry[swp_idx]
#         return self.arry


# 存在重复元素
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(Counter(nums)) != len(nums)

# 数组中的第K个最大元素
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#         heapq.heapify(nums)

# 最小栈
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#
#
#     def pop(self) -> None:
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return min(self.stack)


# 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        stack = []
        for i, n in enumerate(nums):
            while stack and i - stack[0] > k - 1:
                stack.pop(0)
            while stack and n > nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            if i >= k - 1:
                res[i - k + 1] = nums[stack[0]]
        return res


s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
