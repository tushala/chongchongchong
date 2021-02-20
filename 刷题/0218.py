# -*- coding: utf-8 -*-
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 计算右侧小于当前元素的个数


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        arr = [(idx, n) for idx, n in enumerate(nums)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            tmp = []
            i, j = 0, 0
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    res[left[i][0]] += j
                    tmp.append(left[i])
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            return tmp

        merge_sort(arr)
        return res


s = Solution()
print(s.countSmaller([5, 2, 6, 1]))
# print(s.countSmaller([5, 2]))
# 至少有K个重复字符的最长子串


# class Solution(object):
#     def longestSubstring(self, s, k):
#         if not s:
#             return 0
#         for _s in set(s):
#             if s.count(_s) < k:
#                 return max(self.longestSubstring(ss, k) for ss in s.split(_s))
#
#         return len(s)

# 二叉树中的最大路径和
# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         res = float("-inf")
#
#         def getsum(root):
#             nonlocal res
#             if not root:
#                 return 0
#             else:
#                 l = max(0, getsum(root.left))
#                 r = max(0, getsum(root.right))
#
#                 res = max(res, l + r + root.val)
#                 return root.val + max(l, r)
#
#         getsum(root)
#         return res

# 最长连续序列


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         s = set()
#         nums_ = set(nums)
#         res = 0
#         for n in nums_:
#             if n in s:
#                 continue
#             else:
#                 s.add(n)
#                 cur = 1
#                 left, right = n - 1, n + 1
#                 while left in nums_:
#                     cur += 1
#                     left -= 1
#                     s.add(left)
#                 while right in nums_:
#                     cur += 1
#                     right += 1
#                     s.add(right)
#                 res = max(res, cur)
#         return res

# 加油站

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         total, cur_s, start = 0, 0, 0
#
#         for i in range(len(gas)):
#             total += gas[i] - cost[i]
#             cur_s += gas[i] - cost[i]
#             if cur_s < 0:
#                 cur_s = 0
#                 start = i + 1
#         return -1 if total < 0 else start


# 划分字母区间


# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         res = []
#         left, right = 0, 0
#         for i, s in enumerate(S):
#             if i > right:
#                 res.append(right - left + 1)
#                 left, right = i, i
#             ridx = S.rindex(s)
#             if ridx > right:
#                 right = ridx
#
#         res.append(right - left + 1)
#         return res
