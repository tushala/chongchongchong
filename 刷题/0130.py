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

# 剑指offer-51：数组中的逆序对
"""
预备知识

「归并排序」是分治思想的典型应用，它包含这样三个步骤：

分解： 待排序的区间为 [l, r][l,r]，令 m = \lfloor \frac{l + r}{2} \rfloorm=⌊ 
2
l+r
​	
 ⌋，我们把 [l, r][l,r] 分成 [l, m][l,m] 和 [m + 1, r][m+1,r]
解决： 使用归并排序递归地排序两个子序列
合并： 把两个已经排好序的子序列 [l, m][l,m] 和 [m + 1, r][m+1,r] 合并起来
在待排序序列长度为 11 的时候，递归开始「回升」，因为我们默认长度为 11 的序列是排好序的。

思路

那么求逆序对和归并排序又有什么关系呢？关键就在于「归并」当中「并」的过程。我们通过一个实例来看看。假设我们有两个已排序的序列等待合并，分别是 L = \{ 8, 12, 16, 22, 100 \}L={8,12,16,22,100} 和 R = \{ 9, 26, 55, 64, 91 \}R={9,26,55,64,91}。一开始我们用指针 lPtr = 0 指向 LL 的首部，rPtr = 0 指向 RR 的头部。记已经合并好的部分为 MM。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = []
     |                          |
   lPtr                       rPtr
我们发现 lPtr 指向的元素小于 rPtr 指向的元素，于是把 lPtr 指向的元素放入答案，并把 lPtr 后移一位。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8]
        |                       |
      lPtr                     rPtr
这个时候我们把左边的 8 加入了答案，我们发现右边没有数比 8 小，所以 8 对逆序对总数的「贡献」为 0。

接着我们继续合并，把 9 加入了答案，此时 lPtr 指向 12，rPtr 指向 26。


L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8, 9]
        |                          |
       lPtr                       rPtr
此时 lPtr 比 rPtr 小，把 lPtr 对应的数加入答案，并考虑它对逆序对总数的贡献为 rPtr 相对 RR 首位置的偏移 11（即右边只有一个数比 12 小，所以只有它和 12 构成逆序对），以此类推。

我们发现用这种「算贡献」的思想在合并的过程中计算逆序对的数量的时候，只在 lPtr 右移的时候计算，是基于这样的事实：当前 lPtr 指向的数字比 rPtr 小，但是比 RR 中 [0 ... rPtr - 1] 的其他数字大，[0 ... rPtr - 1] 的其他数字本应当排在 lPtr 对应数字的左边，但是它排在了右边，所以这里就贡献了 rPtr 个逆序对。

利用这个思路，我们可以写出如下代码。


在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数
"""
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
#         print(12345, nums[l:r+1])
#         return inv_count
#
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         tmp = [0] * n
#         return self.mergeSort(nums, tmp, 0, n - 1)
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        result = self.reversePairs(left) + self.reversePairs(right)

        # union left and right
        left.sort()
        right.sort()
        index = 0
        for j in range(len(right)):
            while index < len(left) and left[index] <= right[j]:
                index += 1
            result += (len(left) - index)
        return result


s = Solution()
print(s.reversePairs([7, 5, 6, 4, 8, 3, 9, 2]))
# print(s.reversePairs([7, 5, 6, 4]))
# print(s.reversePairs([7, 5]))
# 148. 排序链表
# class Solution:
#     def sortList(self, head: ListNode) -> ListNode:
#         def sortf(h, t):
#             if not h:
#                 return None
#             if h.next == t:
#                 h.next = None
#                 return h
#             slow, fast = h, h
#             while fast != t:
#                 slow = slow.next
#                 fast = fast.next
#                 if fast != t:
#                     fast = fast.next
#             mid = slow
#             return merge(sortf(h, mid), sortf(mid, t))
#
#         def merge(h1, h2):
#             x = ListNode(0)
#             d, a, b = x, h1, h2
#             while a and b:
#                 if a.val > b.val:
#                     d.next = b
#                     b = b.next
#                 else:
#                     d.next = a
#                     a = a.next
#                 d = d.next
#             if a:
#                 d.next = a
#             elif b:
#                 d.next = b
#             return x.next
#
#         return sortf(head, None)


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
