# -*- coding: utf-8 -*-
from typing import *

# 654. 最大二叉树
"""
就这？
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         m = max(nums)
#         idx = nums.index(m)
#         left = nums[:idx]
#         right = nums[idx + 1:]
#         root = TreeNode(m)
#         root.left = self.constructMaximumBinaryTree(left)
#         root.right = self.constructMaximumBinaryTree(right)
#         return root

# 字符串相加
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         n1 = list(num1)
#         n2 = list(num2)
#         carry = 0
#         res = ""
#         while n1 or n2 or carry:
#             l1 = int(n1.pop()) if n1 else 0
#             l2 = int(n2.pop()) if n2 else 0
#             s = carry + l1 + l2
#             carry = s // 10
#             s = s % 10
#             res = str(s) + res
#         return res

# 验证回文字符串 Ⅱ
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# class Solution:
#
#     def validPalindrome(self, s: str) -> bool:
#         if self.ishw(s):
#             return True
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] == s[right]:
#                 left += 1
#                 right -= 1
#             else:
#                 return self.ishw(s[:left] + s[left + 1:]) or self.ishw(s[:right] + s[right + 1:])
#
#         return True
#
#     @staticmethod
#     def ishw(word):
#         return word == word[::-1]

# 乘积最大子数组
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res = nums[0]
#         length = len(nums)
#         big = [nums[0]] * length
#         small = [nums[0]] * length
#         for i, n in enumerate(nums):
#             if not i:
#                 continue
#             else:
#                 big[i] = max(n, big[i - 1] * n, small[i - 1] * n)
#                 small[i] = min(n, big[i - 1] * n, small[i - 1] * n)
#             res = max(res, big[i])
#         return res
