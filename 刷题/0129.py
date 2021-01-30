# -*- coding: utf-8 -*- 
from typing import *

# 543
"""
给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

"""

#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         res = 0
#
#         def dfs(r: TreeNode):
#             nonlocal res
#             if not r:
#                 return 0
#             leftd = dfs(r.left)
#             rightd = dfs(r.right)
#             res = max(res, leftd + rightd)
#             return max(leftd, rightd) + 1
#
#         dfs(root)
#         return res

# 15
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

"""

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         n = len(nums)
#         for i in range(len(nums) - 2):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             left, right = i + 1, n - 1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 elif nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 else:
#                     res.append([nums[i], nums[left], nums[right]])
#                     while left < right and nums[left] == nums[left + 1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right - 1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#         return res
"""
923. 三数之和的多种可能
给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的元组 i, j, k 的数量。

由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。

 

示例 1：

输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举（A[i]，A[j]，A[k]）：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：

输入：A = [1,1,2,2,2,2], target = 5
输出：12
解释：
A[i] = 1，A[j] = A[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
"""
from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        res = 0
        arr.sort()
        length = len(arr)
        c = Counter(arr)
        for i in range(length):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            left, right = i + 1, length - 1
            while left < right:
                if arr[i] + arr[left] + arr[right] > target:
                    right -= 1
                elif arr[i] + arr[left] + arr[right] < target:
                    left += 1
                else:
                    if arr[left] == arr[right] == arr[i]:
                        n = c[arr[i]]
                        res += (n * (n - 1) * (n - 2)) // 6
                    elif arr[left] == arr[i]:
                        n = c[arr[i]]
                        res += (n * (n - 1)) // 2 * c[arr[right]]
                    elif arr[left] == arr[right]:
                        n = c[arr[left]]
                        res += (n * (n - 1)) // 2 * c[arr[i]]
                    else:
                        res += c[arr[i]] * c[arr[left]] * c[arr[right]]
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res % (10 ** 9 + 7)


s = Solution()
print(s.threeSumMulti([1, 1, 2, 2, 2, 2], 5))
print(s.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
