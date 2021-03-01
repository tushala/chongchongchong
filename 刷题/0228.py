# -*- coding: utf-8 -*- 
from typing import *


# 剑指 Offer 24. 反转链表
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         nxt, pre = None, None
#         p = head
#         while p:
#             nxt = p.next
#             p.next = pre
#             pre = p
#             p = nxt
#         return pre


# 剑指 Offer 03. 数组中重复的数字
# class Solution:
#     def findRepeatNumber(self, nums: List[int]) -> int:
#         """二分做"""
#         length = len(nums)
#         left, right = 0, length - 1
#         while left < right:
#             mid = (left + right) // 2
#             t = sum(i <= mid for i in nums)
#             if t > mid + 1:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left


# 剑指 Offer 42. 连续子数组的最大和
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = nums[0]
#         cur = nums[0]
#         for n in nums[1:]:
#             cur = max(cur, 0) + n
#             res = max(res, cur)
#         return res

# 剑指 Offer 22. 链表中倒数第k个节点
# class Solution:
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
#         slow, fast = head,head
#         for i in range(k):
#             fast = fast.next
#         while fast:
#             slow = slow.next
#             fast = fast.next
#         return slow

# 剑指 Offer 38. 字符串的排列
# class Solution:
#     def permutation(self, s: str) -> List[str]:
#         def helper(s):
#             if len(s) == 1:
#                 return [s]
#             else:
#                 res = set()
#                 _res = helper(s[1:])
#                 for r in _res:
#                     for i in range(len(r)+1):
#                         res.add(r[:i] + s[0] + r[i:])
#                 return list(res)
#         return helper(s)


# 合并两个排序的链表
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         w = p = ListNode(0)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 p.next = l1
#                 l1 = l1.next
#                 p = p.next
#             else:
#                 p.next = l2
#                 l2 = l2.next
#                 p = p.next
#         if l1:
#             p.next = l1
#         if l2:
#             p.next = l2
#         return w.next

# 单调数列
# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:
#         inc, dec = False, False
#         for i in range(len(A) - 1):
#             if A[i] > A[i+1]:
#                 dec = True
#             if A[i] < A[i+1]:
#                 inc = True
#         return inc + dec < 2


