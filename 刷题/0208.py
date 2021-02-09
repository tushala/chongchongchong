# -*- coding: utf-8 -*-
from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1019. 链表中的下一个更大节点

# class Solution:
#     def nextLargerNodes(self, head: ListNode) -> List[int]:
#         if not head:
#             return []
#         p = head
#         res = [0] * 10000
#         stack = []
#         num = 0
#         while p:
#             val = p.val
#             while stack and val > stack[-1][-1]:
#                 idx, _ = stack.pop()
#                 res[idx] = val
#             stack.append((num, val))
#             num += 1
#             p = p.next
#         return res[:num]


# 100. 相同的树

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if not p and not q:
#             return True
#         elif not p and q:
#             return False
#         elif not q and p:
#             return False
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 1290. 二进制链表转整数

# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         res = 0
#         p = head
#         while p:
#             res  = res * 2 + p.val
#             p = p.next
#         return res
# 122. 买卖股票的最佳时机 II

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 res += prices[i] - prices[i - 1]
#         return res


# 剑指 Offer 47. 礼物的最大价值
# 
# class Solution:
#     def maxValue(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         dp = [[0] * (1 + n) for _ in range(1 + m)]
# 
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
# 
#         return dp[-1][-1]
