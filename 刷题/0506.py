# -*- coding: utf-8 -*-
from typing import *

# https://leetcode-cn.com/company/bytedance/problemset/


# 接雨水
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         stack = []
#         for i, h in enumerate(height):
#             while stack and h > height[stack[-1]]:
#                 t = stack.pop()
#                 if not stack:
#                     break
#                 left = stack[-1]
#                 c_width = i - left - 1
#                 c_height = min(h, height[left]) - height[t]
#                 res += c_height * c_width
#             stack.append(i)
#         return res

# 整数转罗马数字
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         m = [
#             ['', 'M', 'MM', 'MMM'],
#             ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
#             ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
#             ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
#         ]
#
#         d = [1000, 100, 10, 1]
#         res = ''
#         for i, v in enumerate(d):
#             res += m[i][num // v]
#             num = num % v
#         return res

# 罗马数字转整数

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         res = 0
#         d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         for i in range(len(s)):
#             if i+1 < len(s) and d[s[i]] < d[s[i+1]]:
#                 res -= d[s[i]]
#             else:
#                 res += d[s[i]]
#         return res


# 排序数组
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
# def quick_sort(nums, left, right):
#     if left > right:
#         return
#     l, r = left, right
#     mid = nums[(l + r) // 2]
#     while l <= r:
#         while l <= r and nums[l] < mid:
#             l += 1
#         while l <= r and nums[r] > mid:
#             r -= 1
#         if l <= r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
#     quick_sort(nums, left, r)
#     quick_sort(nums, l, right)
#
# quick_sort(nums, 0, len(nums) - 1)
# return nums


# 字典序的第K小数字
"""
输入:
n: 13   k: 2

输出:
10

解释:
字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
"""


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(c1, c2, n):
            steps = 0
            while c1 <= n:
                steps += min(n + 1, c2) - c1
                c1 *= 10
                c2 *= 10
            return steps

        cur = 1
        k = k - 1
        while k > 0:
            steps = count(cur, cur + 1, n)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur

s = Solution()
print(s.findKthNumber(13, 2))
from transformers import BertModel