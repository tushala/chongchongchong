# -*- coding: utf-8 -*- 
# https://leetcode-cn.com/leetbook/read/bytedance-c01/
from typing import *

# 从前序与中序遍历序列构造二叉树
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         r = preorder[0]
#         idx = inorder.index(r)
#         root = TreeNode(r)
#         root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
#         root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
#         return root

# 阶乘后的零
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         res = 0
#         while n:
#             res += n // 5
#             n //= 5
#         return res


# 古生物血缘远近判定

# 编辑距离
# def edit_distance(s1, s2):
#     len1, len2 = len(s1), len(s2)
#     dp = [[i+j for j in range(len2+1)]for i in range(len1+1)]
#     for i in range(1, len1 + 1):
#         for j in range(1, len2 + 1):
#             e = s1[i-1] != s2[j-1]
#             dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1] + e)
#
#     return dp[-1][-1]

# 最大矩形
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         def cal_max(heights: List):
#             res = 0
#             stack = []
#             heights = [0] + heights + [0]
#             for i in range(len(heights)):
#                 while stack and heights[stack[-1]] > heights[i]:
#                     tmp = stack.pop()
#                     res = max(res, (i - stack[-1] - 1) * heights[tmp])
#                 stack.append(i)
#             return res
#
#         if not matrix:
#             return 0
#         res = 0
#         m, n = len(matrix), len(matrix[0])
#         pre = [[0] * (n + 1) for _ in range(m + 1)]
#
#         for i in range(m):
#             for j in range(n):
#                 pre[i + 1][j] = pre[i][j] + 1 if matrix[i][j] == '1' else 0
#
#         for i in range(1, m + 1):
#             res = max(res, cal_max(pre[i]))
#
#         return res


# 排列序列
# import math
#
#
# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         def helper(s: set, k):
#             length = len(s)
#
#             s_l = list(s)
#             if len(s_l) == 1:
#                 return str(s_l[0])
#             f = math.factorial(length - 1)
#             left_num = k // f
#             s.remove(s_l[left_num])
#             return str(s_l[left_num]) + helper(s, k % f)
#
#         s = set(range(1, n + 1))
#         return helper(s, k - 1)


#  买卖股票的最佳时机
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minp = prices[0]
#         res = float("-inf")
#         for p in prices[1:]:
#             minp = min(p, minp)
#             res = max(res, p-minp)
#         return res

from math import factorial


# 子数组的最小值之和
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         inf = float("-inf")
#         mod = 10 ** 9 + 7
#         arr = arr + [inf]
#         res = 0
#         stack = [-1]
#         for n, a in enumerate(arr):
#             while stack and a < arr[stack[-1]]:
#                 idx = stack.pop()
#                 res += arr[idx] * (n - idx) * (idx-stack[-1])
#             stack.append(n)
#         # print(res)
#         return res % mod

#  预测赢家
# from functools import lru_cache
#
#
# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         @lru_cache(None)
#         def helper(nums):
#             if not len(nums):
#                 return 0
#             left = nums[0] - helper(nums[1:])
#             right = nums[-1] - helper(nums[:-1])
#             return max(left, right)
#
#         return helper(tuple(nums)) >= 0


# 电话号码的字母组合
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         key = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#
#         def helper(digits):
#             if not digits:
#                 return ['']
#             left, right = digits[0], digits[1:]
#             res = []
#             _res = helper(right)
#             for v in key[left]:
#                 res.extend([v + i for i in _res])
#             return res
#         return helper(digits)


#  整数反转

# class Solution(object):
#     def reverse(self, x):
#         sign = x < 0 and -1 or 1
#         x = abs(x)
#         ans = 0
#         while x:
#             ans = ans * 10 + x % 10
#             x //= 10
#
#         return sign * ans if ans <= 0x7fffffff else 0


# 最长回文子串
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def ishuiwen(s):
#             return s == s[::-1]
#
#         res = s[0]
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if s[i] == s[j] and j - i + 1 > len(res):
#                     if sishuiwen(s[i:j + 1]):
#                         res = s[i:j + 1]
#         return res

# 编辑距离
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         len1, len2 = len(word1), len(word2)
#         dp = [[i + j for j in range(len2 + 1)] for i in range(len1 + 1)]
#         for i in range(1, len1 + 1):
#             for j in range(1, len2 + 1):
#                 eq = word1[i - 1] != word2[j - 1]
#                 dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + eq)
#         return dp[-1][-1]


# LRU 缓存机制
# from collections import OrderedDict
#
#
# class LRUCache(OrderedDict):
#
#     def __init__(self, capacity: int):
#         super(LRUCache, self).__init__()
#         self.cap = capacity
#
#     def get(self, key: int) -> int:
#         if key in self:
#             self.move_to_end(key)
#             return self[key]
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.cap:
#             self.popitem(last=False)

# 大礼包
# from functools import lru_cache
#
#
# class Solution:
#     def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
#         @lru_cache(None)
#         def helper(t):
#             # if any(i < 0 for i in t):
#             #     return float("inf")
#             if sum(t) == 0:
#                 return 0
#             res = sum(p * l for p, l in zip(price, t))  # 最大
#             for s in special:
#                 s_, p_ = s[:-1], s[-1]
#
#                 max_choice = min((_t + 0.1) // (_s + 0.01) for _t, _s in zip(t, s_))
#                 if max_choice > 0:
#                     for j in range(1, int(max_choice) + 1):
#                         nt = [i - j * n for i, n in zip(t, s_)]
#                         res = min(res, j * p_ + helper(tuple(nt)))
#             return res
#
#         return helper(tuple(needs))

# 数组组成最大数
# class cmp(str):
#     def __lt__(self, a):
#         return self + a < a + self
#
#
# def comb(xs):
#     xs = map(str, xs.split(','))
#     xs = sorted(xs, key=cmp, reverse=True)
#     return "".join(xs)

# 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def helper(l, r, s):
            if l > n or r > n or r > l:
                return
            if l == n and r == n:

                res.add(s)
                return 
            helper(l+1, r, s+"(")
            helper(l, r+1, s+")")

        helper(0, 0, "")
        return list(res)


