# -*- coding: utf-8 -*- 
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 四数相加 II
# from collections import Counter
# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#         c1 = Counter()
#         c2 = Counter()
#         for i in range(len(A)):
#             for j in range(len(B)):
#                  c1[A[i] + B[j]] += 1
#
#         for i in range(len(C)):
#             for j in range(len(D)):
#                  c2[C[i] + D[j]] += 1
#
#         res = 0
#         for k, v in c1.items():
#             if -k in c2:
#                 res += v*c2[-k]
#         return res

# 常数时间插入、删除和获取随机元素
# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.d = set()
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.d:
#             self.d.add(val)
#             return True
#         return False
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val not in self.d:
#             return False
#         self.d.remove(val)
#         return True
#
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         import random
#         return random.choice(list(self.d))

# 二叉搜索树中第K小的元素
# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         stack = []
#         while True:
#             while root:
#                 stack.append(root)
#                 root = root.left
#
#             root = stack.pop()
#             k -= 1
#             if not k:
#                 return root.val
#             root = root.right


