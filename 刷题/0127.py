# -*- coding: utf-8 -*- 
from typing import *

# 2
"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         res = ListNode(0)
#         carry = 0
#         r = res
#         while l1 or l2:
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             s = x + y + carry
#             carry = s // 10
#             r.next = ListNode(s % 10)
#             r = r.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         if carry:
#             r.next = ListNode(1)
#         return res.next


# if __name__ == '__main__':
#     s = Solution()
#     l1 = ListNode(1)
#     l2 = ListNode(2)
#     l3 = ListNode(3)
#     l4 = ListNode(4)
#     l5 = ListNode(5)
#     l1.next = l2
#     l2.next = l3
#     l4.next = l5
#     res = s.addTwoNumbers(l1, l4)
#     while res:
#         print(res.val, end=" ")
#         res = res.next

# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         # res, cur = nums[0], nums[0]
#         # for i in range(1, len(nums)):
#         #     if cur > 0:
#         #         cur += nums[i]
#         #     else:
#         #         cur = nums[i]
#         #     res = max(res, cur)
#         # return res
#         dp = [float("-inf")] * len(nums)
#         dp[0] = nums[0]
#         res = nums[0]
#         for i in range(1, len(nums)):
#             dp[i] = max(dp[i - 1] + nums[i], nums[i])
#             res = max(res, dp[i])
#         return res
#
#
# s = Solution()
# print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
"""
合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。


示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

"""

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         n1 = nums1[:]
#         s1, s2 = 0, 0
#         idx = 0
#         while s1 < m and s2 < n:
# 
#             if n1[s1] < nums2[s2]:
#                 nums1[idx] = n1[s1]
#                 s1 += 1
#             else:
#                 nums1[idx] = nums2[s2]
#                 s2 += 1
#             idx += 1
#         nums1[idx:m+n] = n1[s1:m] + nums2[s2:n]
#         # print(nums1)
# 
# 
# s = Solution()
# print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))

# 127
"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# 
# class Solution:
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         def get_path(r: TreeNode):
# 
#             if not r:
#                 return []
#             if not r.left and not r.right:
#                 return [[str(r.val)]]
#             lres = get_path(r.left)
#             rres = get_path(r.right)
#             res = []
#             if lres:
#                 for i in lres:
#                     res.append([str(r.val)] + i)
#             if rres:
#                 for i in rres:
#                     res.append([str(r.val)] + i)
#             return res
# 
#         path = get_path(root)
#         return ["->".join(i) for i in path]


# todo
# 缺练 还是菜
