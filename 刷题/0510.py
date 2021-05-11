# -*- coding: utf-8 -*-
# https://codetop.cc/#/home
from typing import *


# 反转链表
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre = None
#         p = head
#         while p:
#             nxt = p.next
#             p.next = pre
#             pre = p
#             p = nxt
#         return pre


# LRU 缓存机制
# from collections import OrderedDict
# class LRUCache(OrderedDict):
#
#     def __init__(self, capacity: int):
#         super(LRUCache, self).__init__()
#         self.cap = capacity
#
#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         else:
#             self.move_to_end(key)
#             return self[key]
#
#     def put(self, key: int, value: int) -> None:
#         self[key] = value
#         self.move_to_end(key)
#
#         if len(self) > self.cap:
#             self.popitem(last=False)

#  最大子序和
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = float("-inf")
#         cur = 0
#         for n in nums:
#             cur = max(n, cur+n)
#             res = max(res, cur)
#         return res


# 数组中的第K个最大元素
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def maxHeapify(a, i, heapSize):
            l, r, largest = i * 2 + 1, i * 2 + 2, i
            if l < heapSize and a[l] > a[largest]:
                largest = l
            if r < heapSize and a[r] > a[largest]:
                largest = r
            if largest != i:
                a[i], a[largest] = a[largest], a[i]
                maxHeapify(a, largest, heapSize)

        def buildMaxHeap(a, heapSize):
            for i in range(heapSize // 2, -1, -1):
                maxHeapify(a, i, heapSize)

        heapSize = len(nums)
        buildMaxHeap(nums, heapSize)
        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapSize -= 1
            maxHeapify(nums, 0, heapSize)
        return nums[0]


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], k=2))
print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))

# 无重复字符的最长子串
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         left = 0
#         d = {}
#         for n, _s in enumerate(s):
#             if _s in d:
#                 while _s in d:
#                     del d[s[left]]
#                     left += 1
#             d[_s] = 1
#
#             res = max(res, n-left+1)
#         return res

# 两数之和
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         for i, n in enumerate(nums):
#             if target - n in d:
#                 return [i, d[target-n]]
#             d[n] = i
#

# 合并两个有序链表

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         res = p = ListNode(0)
#         while l1 and l2:
#             if l1.val >= l2.val:
#                 p.next = l2
#                 l2 = l2.next
#             else:
#                 p.next = l1
#                 l1 = l1.next
#             p = p.next
#         if l1:
#             p.next = l1
#         if l2:
#             p.next = l2
#         return res.next


# 买卖股票的最佳时机

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         buy = prices[0]
#         for p in prices[1:]:
#             buy = min(buy, p)
#             res = max(res, p-buy)
#         return res

