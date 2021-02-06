# -*- coding: utf-8 -*- 
from typing import *
from functools import lru_cache


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 面试题 02.06. 回文链表

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         if not head:
#             return True
#         mid = self.getmid(head)
#         mid = self.reverse(mid)
#         return self.judge(head, mid)
#
#     def getmid(self, head):
#         slow, fast = head, head
#         while fast.next:
#             slow = slow.next
#             fast = fast.next
#             if fast.next:
#                 fast = fast.next
#         return slow
#
#     def reverse(self, head):
#         pre = None
#         cur = head
#         while cur:
#             nxt = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nxt
#         return pre
#
#     def judge(self, p1, p2):
#         while p2:
#             if p1.val != p2.val:
#                 return False
#             p1 = p1.next
#             p2 = p2.next
#         return True

# 字符串专题 https://leetcode-cn.com/leetbook/read/top-interview-questions/xmolhc/
# 验证回文串

# class Solution:
#     def ischar(self, x):
#         return '0' <= x <= '9' or 'a' <= x <= 'z'
#
#     def isPalindrome(self, s: str) -> bool:
#         if not s:
#             return True
#         s = s.lower()
#         left, right = 0, len(s) - 1
#         while left < right:
#             while left < right and not self.ischar(s[left]):
#                 left += 1
#             while left < right and not self.ischar(s[right]):
#                 right -= 1
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True


# class Solution:
#     def ishw(self, x):
#         return x == x[::-1]
#
#     @lru_cache(None)
#     def partition(self, s: str) -> List[List[str]]:
#         if not s:
#             return [[]]
#         if len(s) == 1:
#             return [[s]]
#
#         res = []
#         for i in range(len(s)):
#             left, right = s[:i+1], s[i+1:]
#             if self.ishw(left):
#                 _ans = self.partition(right)
#                 ans = [[left] + i for i in _ans]
#                 res.extend(ans)
#         return res

# 单词拆分

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#
#         @lru_cache(None)
#         def _wordBreak(s: str) -> bool:
#             if not s:
#                 return True
#             for i in range(len(s)):
#                 left = s[:i + 1]
#                 if left in wordDict and _wordBreak(s[i + 1:]):
#                     return True
#
#             return False
#
#         return _wordBreak(s)

# 单词拆分 II


# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         @lru_cache(None)
#         def _wordBreak(s: str):
#             if not s:
#                 return [[]]
#             res = []
#             for i in range(len(s)):
#                 left = s[:i + 1]
#                 if left in wordDict:
#                     _ans = _wordBreak(s[i + 1:])
#                     ans = [[left] + i for i in _ans]
#                     res.extend(ans)
#
#             return res
#         res = _wordBreak(s)
#         return [" ".join(i) for i in res]
