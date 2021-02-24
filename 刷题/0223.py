# -*- coding: utf-8 -*- 
from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 只出现一次的数字

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         r = 0
#         for n in nums:
#             r ^= n
#         return r

# 直线上最多的点数


# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         def get_k_b(p1, p2):
#             ...
#         for i in range()

# 环形链表

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if head is None or head.next is None:
#             return False
#         slow, fast = head, head.next
#         while fast and fast.next and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False


# 排序链表
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         return self.sortf(head, None)
#
#     def sortf(self, head, tail):
#         if not head:
#             return None
#         if head.next == tail:
#             head.next = None
#             return head
#         mid = self.getmid(head, tail)
#         left = self.sortf(head, mid)
#         right = self.sortf(mid, tail)
#         return self.merge(left, right)
#
#     def getmid(self, head, tail):
#         slow, fast = head, head
#         while fast != tail:
#             slow = slow.next
#             fast = fast.next
#             if fast != tail:
#                 fast = fast.next
#
#         mid = slow
#         return mid
#
#     @staticmethod
#     def merge(left, right):
#         p1, p2 = left, right
#         m = p = ListNode(0)
#         while p1 and p2:
#             if p1.val < p2.val:
#                 p.next = p1
#                 p1 = p1.next
#             else:
#                 p.next = p2
#                 p2 = p2.next
#             p = p.next
#         if p1:
#             p.next = p1
#         elif p2:
#             p.next = p2
#         return m.next

# 相交链表
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if headA is None or headB is None:
#             return None
#         ha = headA
#         hb = headB
#         while ha != hb:
#             ha = ha.next if ha else headB
#             hb = hb.next if hb else headA
#         return ha
# a, b = headA, headB
# while a and b:
#     a = a.next
#     b = b.next
# if a is None:
#     s1 = headA
#     s2 = b
# else:
#     s1 = a
#     s2 = headB
# while s1 and s2:
#     if s1 == s2:
#         return s1
#     s1 = s1.next
#     s2 = s2.next
# return None

# 反转链表
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
# pre = None
# p = head
# while p:
#     nxt = p.next
#     p.next = pre
#     pre = p
#     p = nxt
#
# return pre
# if not head or not head.next:
#     return head
# r = self.reverseList(head.next)
# head.next.next = head
# head.next = None
# return r

# 滑动窗口中位数
"""
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：

[2,3,4]，中位数是 3
[2,3]，中位数是 (2 + 3) / 2 = 2.5
给你一个数组 nums，有一个长度为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。
示例：

给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

[1,-1,-1,3,5,6]
"""

import collections, heapq
class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0

    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap: List[int]):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break

    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.makeBalance()

    def erase(self, num: int):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.makeBalance()

    def getMedian(self) -> float:
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        ans = [dh.getMedian()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.getMedian())

        return ans




s = Solution()
print(s.medianSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
