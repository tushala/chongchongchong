# -*- coding: utf-8 -*-
from typing import *


# 633
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         left, right = 0, int(c ** 0.5)
#         while left <= right:
#             t = left**2 +  right**2
#             if t == c:
#                 return True
#             elif t > c:
#                 right -= 1
#             else:
#                 left += 1
#         return False


# 283
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         z = 0
#         for idx, n in enumerate(nums):
#             if n != 0:
#                 nums[idx], nums[z] = nums[z], nums[idx]
#                 z += 1


class AllSortSolution:

    @staticmethod
    def bubbleSort(x):
        # 冒泡
        for i in range(len(x)):
            for j in range(i):
                if x[j] > x[i]:
                    x[i], x[j] = x[j], x[i]

    @staticmethod
    def selectSort(x):
        # 选择排序
        for i in range(len(x) - 1):
            minidx = i
            for j in range(i + 1, len(x)):
                if x[minidx] > x[j]:
                    minidx = j

            x[i], x[minidx] = x[minidx], x[i]

    @staticmethod
    def insertSort(x):
        # 选择排序
        for i in range(1, len(x)):
            j = i
            while j >= 1 and x[j] < x[j - 1]:
                x[j], x[j - 1] = x[j - 1], x[j]
                j -= 1

    @staticmethod
    def shellinsertSort(x):
        length = len(x)
        step = length // 2
        while step > 0:
            for i in range(step, length):
                while i >= step and x[i - step] > x[i]:
                    x[i], x[i - step] = x[i - step], x[i]
                    i -= step
            step //= 2

    def mergeSort(self, x):
        if len(x) <= 1:
            return x

        def merge(l1, l2):
            idx1, idx2 = 0, 0
            res = []
            while idx1 < len(l1) and idx2 < len(l2):
                if l1[idx1] < l2[idx2]:
                    res.append(l1[idx1])
                    idx1 += 1
                else:
                    res.append(l2[idx2])
                    idx2 += 1
            res.extend(l1[idx1:])
            res.extend(l2[idx2:])
            return res

        idx = len(x) // 2

        left = self.mergeSort(x[:idx])
        right = self.mergeSort(x[idx:])
        return merge(left, right)

    @staticmethod
    def quick_Sort(x):
        def quick_Sort_(x, left, right):
            if left > right:
                return
            l, r = left, right
            mid = x[(l + r) // 2]
            while l <= r:
                while x[l] < mid:
                    l += 1
                while x[r] > mid:
                    r -= 1
                if l <= r:
                    x[l], x[r] = x[r], x[l]
                    l += 1
                    r -= 1
            quick_Sort_(x, left, r)
            quick_Sort_(x, l, right)

        quick_Sort_(x, 0, len(x) - 1)

    def heap_Sort(self):
        ...


# w = list(range(6, 0, -1))
w = [5, 2, 6, 0, 3, 9, 1, 7, 4, 8]
s = AllSortSolution()

s.shellinsertSort(w)
print(w)
