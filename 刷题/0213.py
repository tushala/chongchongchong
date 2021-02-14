# -*- coding: utf-8 -*- 
from typing import *

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq
#         return heapq.nlargest(k, nums)[-1]


# 数据流的中位数
import bisect
import heapq


# class MedianFinder:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#
#         self.l = []
#
#     def addNum(self, num: int) -> None:
#         bisect.insort_left(self.l, num)
#
#     def findMedian(self) -> float:
#         length = len(self.l)
#         if length % 2:
#             return (self.l[length // 2] + self.l[length // 2 - 1]) / 2
#         else:
#             return self.l[length // 2]

# 有序矩阵中第K小的元素
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n = len(matrix)
        # pq = [(matrix[i][0], i, 0) for i in range(n)]
        # heapq.heapify(pq)
        # for i in range(k - 1):
        #     nums, x, idx = heapq.heappop(pq)
        #     if idx < n - 1:
        #         heapq.heappush(pq, (matrix[x][idx + 1], x, idx + 1))
        # return heapq.heappop(pq)[0]

        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            nums = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    nums += i + 1
                    j += 1
                else:
                    i -= 1
            return nums >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
