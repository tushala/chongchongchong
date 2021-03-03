# -*- coding: utf-8 -*- 
from typing import *

# 剑指 Offer 10- II.
# class Solution:
#     def numWays(self, n: int) -> int:
#         d = {0: 1, 1: 1}
#         for i in range(2, n + 1):
#             d[i] = (d[i - 1] + d[i - 2]) % (1e9 + 7)
#         return d[n]


# 剑指 Offer 48.

from collections import Counter


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         length = len(s)
#         left, right = 0, 0
#         r = Counter()
#         while right < length:
#             r[s[right]] += 1
#             while r[s[right]] > 1:
#                 r[s[left]] -= 1
#                 left += 1
#             right += 1
#             res = max(res, right - left)
#
#         return res

# 剑指 Offer 07

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         r = preorder[0]
#         t = TreeNode(r)
#         idx = inorder.index(r)
#         t.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
#         t.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
#         return t

# 剑指 Offer 52.
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if headA is None or headB is None:
#             return None
#         ha, hb = headA, headB
#         while ha != hb:
#             ha = ha.next if ha else headB
#             hb = hb.next if hb else headA
#         return ha
