# -*- coding: utf-8 -*-
from typing import *


# 最长公共子序列


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         l1, l2 = len(text1), len(text2)
#         dp = [[0] * (1 + l2) for _ in range(2)]
#         for i in range(1, l1 + 1):
#             for j in range(1, l2 + 1):
#                 idx = i % 2
#                 dp[idx][j] = max(dp[idx - 1][j], dp[idx][j - 1], dp[idx - 1][j - 1] + (text1[i - 1] == text2[j - 1]))
#         return dp[l1%2][-1]

# K 个一组翻转链表

# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         def reverse(p: ListNode, t: ListNode):
#             pre = p
#             while p != t:
#                 nxt = p.next
#                 p.next = pre
#                 pre = p
#                 p = nxt
#             return pre
#
#         a, b = head, head
#         for i in range(k):
#             if not b:
#                 return head
#             b = b.next
#         nh = reverse(a, b)
#         a.next = self.reverseKGroup(b, k)
#         return nh

# 二叉树的最大深度
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 最长递增子序列
# from bisect import bisect_left
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         b = []
#         for _, n in enumerate(nums):
#             idx = bisect_left(b, n)
#             if idx == len(b):
#                 b.append(n)
#             else:
#                 b[idx] = n
#         return len(b)

#  合并区间

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
#         res = []
#         left, right = intervals[0]
#         for l, r in intervals:
#             if l > right:
#                 res.append([left, right])
#                 left, right = l, r
#             else:
#                     right = max(r, right)
#         res.append([left, right])
#         return res

# 环形链表
#
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head or not head.next:
#             return False
#         slow, fast = head, head
#         while fast and fast.next and fast.next.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False

# 二叉树的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        elif left is None:
            return right
        return left
