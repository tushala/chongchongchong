# -*- coding: utf-8 -*-
from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 剑指 Offer 45.
# class cmp(str):
#     def __lt__(self, other):
#         return self + other < other + self
#
#
# class Solution:
#     def minNumber(self, nums: [int]) -> str:
#         nums = sorted([str(i) for i in nums], key=cmp)
#         return "".join(nums)

# 3.8 也放这里

# 1774
# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         ans = [10 ** 6, 0]
#
#         def f(i, pre):
#             nonlocal ans
#             if ans[0] == 0:
#                 return
#             for j in range(3):
#                 cost = pre + toppingCosts[i] * j
#                 diff = abs(cost - target)
#                 if diff < ans[0]:
#                     ans = [diff, cost]
#                 elif diff == ans[0]:
#                     ans[1] = min(ans[1], cost)
#                 if pre < target and i < len(toppingCosts) - 1:
#                     f(i + 1, cost)
#
#         for b in baseCosts:
#             f(0, b)
#         return ans[1]


# 132.
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。

 

示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class Solution:
#     def minCut(self, s: str) -> int:
#         length = len(s)
#         g = [[True] * length for _ in range(length)]
#         for i in range(length - 1, -1, -1):
#             for j in range(i + 1, length):
#                 g[i][j] = g[i+1][j-1] and (s[i] == s[j])
#         f = list(range(length))
#         for i in range(length):
#             if g[0][i]:
#                 f[i] = 0
#             else:
#                 for j in range(i):
#                     if g[j+1][i]:
#                         f[i] = min(f[i], f[j] + 1)
#         return f[-1]


# 86
"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

 

示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
 

提示：

"""


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dh1 = ListNode(0)
        dh2 = ListNode(0)
        node1, node2 = dh1, dh2
        while head:
            if head.val < x:
                node1.next = head
                head = head.next
                node1 = node1.next
                node1.next = None
            else:
                node2.next = head
                head = head.next
                node2 = node2.next
                node2.next = None
        node1.next = dh2.next
        return dh1.next


s = Solution()

l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
# r = s.partition(l1, 3)
# while r:
#     print(r.val, end='\t')
#     r = r.next

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
d = {'x': 4, 'y': 5}
p = Point(**d)
print(p)
