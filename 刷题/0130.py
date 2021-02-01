# -*- coding: utf-8 -*-
from typing import *


# 142. 环形链表 II
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return None
#         s = set()
#         res = 0
#         while head is not None:
#             if head in s:
#                 return head
#             else:
#                 head = head.next
#         return None

# 剑指 Offer 24. 反转链表
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         preNode = None
#         currNode = head
#         while currNode:
#             nextNode = currNode.next
#             currNode.next = preNode
#             preNode = currNode
#             currNode = nextNode
#         return preNode


# 剑指 Offer 27. 二叉树的镜像
# class Solution:
#     def mirrorTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None
#         l = self.mirrorTree(root.left)
#         r = self.mirrorTree(root.right)
#         root.left = r
#         root.right = l
#         return root


# 剑指 Offer 26. 树的子结构
# class Solution:
#     def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
#         def pd(A, B):
#             if B is None:
#                 return True
#             if A is None and B is not None:
#                 return False
#             if A.val == B.val and pd(A.left, B.left) \
#                     and pd(A.right, B.right):
#                 return True
#             return False
#         return (bool(A and B)) and (pd(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

# 3. 无重复字符的最长子串
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         d = {}
#         left = 0
#         for n, _s in enumerate(s):
#             if _s not in d:
#                 d[_s] = 1
#             else:
#                 while _s in d:
#                     del d[s[left]]
#                     left += 1
#                 d[_s] = 1
#             res = max(res, n - left+1)
#         return res

# class Solution:
#     def mergeSort(self, nums, tmp, l, r):
#         if l >= r:
#             return 0
#         mid = (l + r) // 2
#         inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
#         i, j, pos = l, mid + 1, l
#         while i <= mid and j <= r:
#             if nums[i] <= nums[j]:
#                 tmp[pos] = nums[i]
#                 i += 1
#                 inv_count += (j - (mid + 1))
#             else:
#                 tmp[pos] = nums[j]
#                 j += 1
#             pos += 1
#         for k in range(i, mid + 1):
#             tmp[pos] = nums[k]
#             inv_count += (j - (mid + 1))
#             pos += 1
#
#         for k in range(j, r + 1):
#             tmp[pos] = nums[k]
#             pos += 1
#         nums[l:r + 1] = tmp[l:r + 1]
#         return inv_count
#
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         tmp = [0] * n
#         return self.mergeSort(nums, tmp, 0, n - 1)


# 148. 排序链表
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortf(h, t):
            if not h:
                return None
            if h.next == t:
                h.next = None
                return h
            slow = fast = h
            while fast != t:
                slow = slow.next
                fast = fast.next
                if fast != t:
                    fast = fast.next
            mid = slow
            return merge(sortf(h, mid), sortf(mid, t))

        def merge(h1, h2):
            x = ListNode(0)
            d, a, b = x, h1, h2
            while a and b:
                if a.val > b.val:
                    d.next = b
                    b = b.next
                else:
                    d.next = a
                    a = a.next
                d = d.next
            if a:
                d.next = a
            elif b:
                d.next = b
            return x.next

        return sortf(head, None)


# s = Solution()
# l1 = ListNode(1)
# l2 = ListNode(4)
# l3 = ListNode(3)
# l4 = ListNode(2)
# l1.next =l2
# l2.next =l3
# l3.next =l4
# print(s.sortList(l1).val)

# 23. 合并K个升序链表
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         def merge(l1, l2):
#             x = ListNode(0)
#             h, t1, t2 = x, l1, l2
#             while t1 and t2:
#                 if t1.val > t2.val:
#                     h.next = t2
#                     t2 = t2.next
#                 else:
#                     h.next = t1
#                     t1 = t1.next
#                 h = h.next
#             if t1:
#                 h.next = t1
#             elif t2:
#                 h.next = t2
#             return x.next
#         res = None
#         for i in range(len(lists)):
#             res = merge(res, lists[i])
#         return res