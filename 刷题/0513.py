# -*- coding: utf-8 -*- 
from typing import *


# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         len1, len2 = len(num1), len(num2)
#         l1, l2 = len1 - 1, len2 - 1
#         carry = 0
#         res = ""
#         while l1 >= 0 or l2 >= 0:
#             n1 = ord(num1[l1]) - ord('0') if l1 >= 0 else 0
#             n2 = ord(num2   [l2]) - ord('0') if l2 >= 0 else 0
#             cur = carry + n1 + n2
#             carry = cur // 10
#             cur = cur % 10
#             res = str(cur) + res
#             l1 -= 1
#             l2 -= 1
#         if carry:
#             res = '1' + res
#
#         return res
s = Solution()
