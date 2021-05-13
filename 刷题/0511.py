# -*- coding: utf-8 -*-

from typing import *


# 数组中的第K个最大元素
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def heapify(a, i, size):
#             l, r, largest = i * 2 + 1, i * 2 + 2, i
#             if l < size and a[l] > a[largest]:
#                 largest = l
#             if r < size and a[r] > a[largest]:
#                 largest = r
#             if largest != i:
#                 a[i], a[largest] = a[largest], a[i]
#                 heapify(a, largest, size)
#
#         def buildheap(nums, size):
#             for i in range(size // 2, -1, -1):
#                 heapify(nums, i, size)
#
#         size = len(nums)
#         buildheap(nums, size)
#
#         for i in range(len(nums) - 1, len(nums) - k, -1):
#             nums[i], nums[0] = nums[0], nums[i]
#             size -= 1
#             heapify(nums, 0, size)
#         return nums[0]

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return None
#         ha = headA
#         hb = headB
#         while ha != hb:
#             ha = ha.next if ha.next else hb
#             hb = ha.next if ha.next else ha
#         return ha

# 分割等和子集
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s % 2 != 0:
#             return False
#         target = s // 2
#         dp = [False] * (1 + target)
#         dp[0] = True
#         for n in nums:
#             for i in range(target, n - 1, -1):
#                 dp[i] = dp[i - n] or dp[i]
#         return dp[-1]

# 三数之和
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []
#         for i in range(len(nums) - 2):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             left, right = i + 1, len(nums) - 1
#             while left < right:
#                 if nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 elif nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 else:
#                     res.append([nums[i], nums[left], nums[right]])
#                     while left < right and nums[left] == nums[left+1]:
#                         left += 1
#                     while left < right and nums[right] == nums[right-1]:
#                         right -= 1
#                     left += 1
#                     right -= 1
#
#         return res


# 面试题 17.14. 最小K个数
# class Solution:
#     def smallestK(self, arr: List[int], k: int) -> List[int]:
#         def heapy(arr, i, size):
#             l, r, largest = i * 2 + 1, i * 2 + 2, i
#             if l < size and arr[l] < arr[largest]:
#                 largest = l
#             if r < size and arr[r] < arr[largest]:
#                 largest = r
#             if largest != i:
#                 arr[i], arr[largest] = arr[largest], arr[i]
#                 heapy(arr, largest, size)
#
#         def builfheap(arr, size):
#             for i in range(size // 2, -1, -1):
#                 heapy(arr, i, size)
#
#         size = len(arr)
#         builfheap(arr, size)
#
#         res = []
#         for i in range(size - 1, size - k - 1, -1):
#             res.append(arr[0])
#             arr[0], arr[i] = arr[i], arr[0]
#             size -= 1
#             heapy(arr, 0, size)
#         return res

# 二分查找

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1

# 有效的括号

# class Solution:
#     def isValid(self, s: str) -> bool:
#         d = {'(': ')', '{': '}', '[': ']'}
#         stack = []
#         for _s in s:
#             if _s in d:
#                 stack.append(_s)
#             else:
#                 if not stack:
#                     return False
#                 last_s = stack.pop()
#                 if d[last_s] != _s:
#                     return False
#         return len(stack) == 0

# 接雨水
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         res = 0
#         stack = []
#         for n, h in enumerate(height):
#             while stack and h > height[stack[-1]]:
#                 t = stack.pop()
#                 if not stack:
#                     break
#                 width = min(h, height[stack[-1]]) - height[t]
#                 length = n - stack[-1] - 1
#                 res += width * length
#             stack.append(n)
#         return res

# 两数相加

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         p = res = ListNode(0)
#         carry = 0
#         while l1 or l2:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
#             val = val1 + val2 + carry
#
#             carry = val // 10
#             val %= 10
#             p.next = ListNode(val)
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#             p = p.next
#         if carry:
#             p.next = ListNode(1)
#         return res.next

# 翻转二叉树
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root :
#             return None
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root
