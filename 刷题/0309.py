# -*- coding: utf-8 -*- 
from typing import *

# 85
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         if not matrix:
#             return 0
#         res = 0
#         m, n = len(matrix), len(matrix[0])
#         pre = [0] * (n + 1)
#         for i in range(m):
#             for j in range(n):
#                 pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0
#
#             stack = [-1]
#             for k, num in enumerate(pre):
#                 while stack and pre[stack[-1]] > num:
#                     index = stack.pop()
#                     res = max(res, pre[index] * (k - stack[-1] - 1))
#                 stack.append(k)
#
#         return res


# 1047
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         stack = []
#         for s in S:
#             if stack and stack[-1] == s:
#                 stack.pop()
#             else:
#                 stack.append(s)
#         return "".join(stack)


# 48

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for i in range(n):
#             for j in range(n // 2):
#                 matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
#


# 201
# class Solution:
#     def rangeBitwiseAnd(self, m: int, n: int) -> int:
#         shift = 0
#         while m != n:
#             m = m >> 1
#             n = n >> 1
#             shift += 1
#         return n << shift


# 89

# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         if n == 0:
#             return [0]
#         ans = [0, 1]
#         for i in range(1, n):
#             for num in ans[::-1]:
#                 ans.append(2 ** i + num)
#         return ans

# 剑指 Offer 57 - II.
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         res = []
#         up = int((target * 2) ** 0.5)
#
#         def getans(a, b):
#             x = (a + b - 1) // 2
#             y = (b - a + 1) // 2
#             return y, x
#
#         for i in range(1, up + 1):
#             if (target * 2) % i == 0:
#                 a, b = i, (target * 2) // i
#                 if (a%2 and not b%2) or(b%2 and not a%2):
#                     l, u = getans(a,b)
#                     if u > l:
#                         res.append(list(range(l, u + 1)))
#         res.sort(key=lambda x: x[0])
#         return res

# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         i, j, s, res = 1, 2, 3, []
#         while i < j:
#             if s == target:
#                 res.append(list(range(i, j + 1)))
#             if s >= target:
#                 s -= i
#                 i += 1
#             else:
#                 j += 1
#                 s += j
#         return res

# 剑指 Offer 55 - I
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 224


# class Solution:
#     def calculate(self, s: str) -> int:
#         res = 0
#         sign = 1
#         stack = []
#         s = s.strip()
#         s = '(' + s + ')'
#         i = 0
#         while i < len(s):
#             if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                 num = 0
#                 while s[i].isdigit() and i < len(s):
#                     num = 10 * num + ord(s[i]) - ord('0')
#                     i += 1
#                 i -= 1
#                 res += num * sign
#             elif s[i] == '+':
#                 sign = 1
#             elif s[i] == '-':
#                 sign = -1
#             elif s[i] == '(':
#                 stack.append([res, sign])
#                 res = 0
#                 sign = 1
#             elif s[i] == ')':
#                 res_, sign_ = stack.pop()
#                 res = sign_ * res + res_
#             i += 1
#         return res
