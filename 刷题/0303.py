# -*- coding: utf-8 -*- 
from typing import *

# 面试题 08.06.


# class Solution:
#     def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
#         """
#         Do not return anything, modify C in-place instead.
#         """
#         n = len(A)
#         self.move(n, A, B, C)
#         # 定义move 函数移动汉诺塔
#
#     def move(self, n, A, B, C):
#         if n == 1:
#             C.append(A[-1])
#             A.pop()
#             return
#         else:
#             self.move(n - 1, A, C, B)  # 将A上面n-1个通过C移到B
#             C.append(A[-1])  # 将A最后一个移到C
#             A.pop()  # 这时，A空了
#             self.move(n - 1, B, A, C)  # 将B上面n-1个通过空的A移到

# 93

# class Solution:
#     def restoreIpAddresses(self, s: str):
#         res = set()
#
#         def getadd(s, n, cur):
#             if len(s) > 3 * n or len(s) < n:
#                 return
#             if not n and not s:
#                 res.add(".".join(cur))
#                 return
#             for i in range(1, 4):
#                 _cur = s[:i]
#                 if 0 <= int(_cur) <= 255:
#                     if len(_cur) == 1 or (not _cur.startswith('0')):
#                         getadd(s[i:], n - 1, cur + (_cur,))
#
#         getadd(s, 4, ())
#         return list(res)

# 剑指 Offer 16
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if x == 0:
#             return 0
#
#         if n < 0:
#             return self.myPow(1/x, -n)
#         res = 1.
#         while n > 0:
#             if n & 1 == 1:
#                 res *= x
#             x *= x
#             n >>= 1
#         return res

# 剑指 Offer 53
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = (left+right) // 2
#             if nums[mid] == mid:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return left
# 剑指 Offer 51
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
"""

# class Solution:
#     def mergeSort(self, nums, tmp, l, r):
#         if l >= r:
#             return 0
#         mid = (l + r) // 2
#         res = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
#         i, j, pos = l, mid + 1, l
#         while i <= mid and j <= r:
#             if nums[i] <= nums[j]:
#                 res += (j - mid - 1)
#                 tmp[pos] = nums[i]
#                 i += 1
#             else:
#                 tmp[pos] = nums[j]
#                 j += 1
#             pos += 1
#         for w in range(i, mid + 1):
#             tmp[pos] = nums[w]
#             res += (j - mid - 1)
#             pos += 1
#         for w in range(j, r + 1):
#             tmp[pos] = nums[w]
#             pos += 1
#         nums[l:r + 1] = tmp[l:r + 1]
#         return res
#
#     def reversePairs(self, nums: List[int]) -> int:
#         n = len(nums)
#         tmp = [0] * n
#         return self.mergeSort(nums, tmp, 0, n - 1)


# 剑指 Offer 14- II
# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         mod = 1000000007
#         if n == 2:
#             return 1
#         elif n == 3:
#             return 2
#         elif n == 4:
#             return 4
#         else:
#             if n % 3 == 0:
#                 return pow(3, n // 3) % mod
#             elif n % 3 == 1:
#                 return (4 * pow(3, (n - 4) // 3)) % mod
#             else:
#                 return 2 * pow(3, (n - 2) // 3) % mod
