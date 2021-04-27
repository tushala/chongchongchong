# -*- coding: utf-8 -*- 
from typing import *
from bisect import bisect_right

# 870
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         A.sort()
#         res = []
#         for b in B:
#             i = bisect_right(A, b)
#             res.append(A.pop(i) if i < len(A) else A.pop(0))
#         return res


# 845

from collections import Counter

# class Solution:
#     def isNStraightHand(self, hand: List[int], W: int) -> bool:
#         if len(hand) % W:
#             return False
#         counter = Counter(hand)
#         while Counter:
#             mink = min(counter.keys())
#             for y in range(mink, mink + W):
#                 if y not in counter:
#                     return False
#                 counter[y] -= 1
#                 if not counter[y]:
#                     del counter[y]
#         return True

# 765. 情侣牵手

# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         length = len(row)
#         res = 0
#         for i in range(0, length, 2):
#             tag = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
#             if row[i+1] != tag:
#                 idx = row.index(tag)
#                 row[i+1], row[idx] = row[idx], row[i+1]
#                 res += 1
#         return res

# 剑指 Offer 21
# class Solution:
#     def exchange(self, nums: List[int]) -> List[int]:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             while left < right and nums[left] % 2 == 1:
#                 left += 1
#             while left < right and nums[right] % 2 == 0:
#                 right -= 1
#             if left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1
#         return nums

# 781

# from collections import Counter
# import math
# class Solution:
#     def numRabbits(self, answers: List[int]) -> int:
#         c = Counter(answers)
#         res = 0
#         for k, v in c.items():
#             res += math.ceil(v/(k+1)) * (k+1)
#         return res

# 790
"""
790. 多米诺和托米诺平铺
有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

XX  <- 多米诺

XX  <- "L" 托米诺
X
给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。

（平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）

示例:
输入: 3
输出: 5
解释: 
下面列出了五种不同的方法，不同字母代表不同瓷砖：
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
"""
# class Solution:
#     def numTilings(self, N: int) -> int:
#         mod = pow(10, 9) +7
#         dp = [0] * (N +1)
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 5
#         for i in range(4, N+1):
#             dp[i] = (dp[i-1] + dp[i-2] *3) % mod
#         return dp[-1]
# s = Solution()
# print(s.exchange([1, 2, 3, 4]))
# print(s.exchange([1,3,5]))

"""
面试题 17.23. 最大黑方阵
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]
"""
# class Solution:
#     def findSquare(self, matrix: List[List[int]]) -> List[int]:


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         def reverse(head: ListNode):
#             pre = None
#             while head:
#                 nxt = head.next
#                 head.next = pre
#                 pre = head
#                 head = nxt
#             return pre
#
#         dimmy = ListNode(0)
#         dimmy.next = head
#         pre = dimmy
#         for i in range(left - 1):
#             pre = pre.next
#
#         right_node = pre
#         for _ in range(right - left + 1):
#             right_node = right_node.next
#         left = pre.next
#         pre.next = None
#         curr = right_node.next
#         right_node.next = None
#         p = reverse(left)
#         left.next = curr
#         pre.next = p
#         return dimmy.next



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def maxLevelSum(self, root: TreeNode) -> int:
#         curnode = [root]
#         layer_num = 0
#         min_s = float("-inf")
#         res = 0
#         while curnode:
#             layer_num += 1
#             nxt_layer = []
#             cur_sum = 0
#             for node in curnode:
#                 cur_sum += node.val
#                 if node.left:
#                     nxt_layer.append(node.left)
#                 if node.right:
#                     nxt_layer.append(node.right)
#             if min_s < cur_sum:
#                 res = layer_num
#                 min_s = cur_sum
#             curnode = nxt_layer
#         return res

from transformers import AdamW
from torch.optim import AdamW
s = Solution()
