# -*- coding: utf-8 -*- 
from typing import *


# 扁平化嵌套列表迭代器
# class NestedIterator:
#     def __init__(self, nestedList):
#         self.stack = nestedList[::-1]
#
#     def next(self) -> int:
#         return self.stack.pop().getInteger()
#
#     def hasNext(self) -> bool:
#         while len(self.stack) > 0 and self.stack[-1].isInteger() is False:
#             self.stack += self.stack.pop().getList()[::-1]
#         return len(self.stack) > 0


# 逆波兰表达式求值
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for i, t in enumerate(tokens):
#             if t in ['+', '-', '*', '/']:
#                 r = stack.pop()
#                 l = stack.pop()
#                 e = int(eval(f"{l}{t}{r}"))
#                 stack.append(e)
#             else:
#                 stack.append(int(t))
#         return stack[0]


# 基本计算器 II
# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = [0]
#         nums = ""
#         ch = "+"
#         for i, n in enumerate(s):
#             if n.isdigit():
#                 nums += n
#             if n in ["+", "-", "*", "/"] or i == len(s) - 1:
#                 v = int(nums)
#                 nums = ""
#                 if ch in ['+', '-']:
#                     stack.append(v * (1 if ch == "+" else -1))
#                 if ch in ["*", "/"]:
#                     ov = stack.pop()
#                     nv = int(eval(f"{ov}{ch}{v}"))
#                     stack.append(nv)
#                 ch = n
#         res = 0
#         for n in stack:
#             res += n
#
#         return res
