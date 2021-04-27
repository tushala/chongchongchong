# -*- coding: utf-8 -*-
from typing import *

# 470
# class Solution:
#     def rand10(self):
#         # while True:
#         #     res = (rand7() - 1) * 7 + rand7()  # 构造1~49的均匀分布
#         #     if res <= 40:  # 剔除大于40的值，1-40等概率出现。
#         #         break
#         # return res % 10 + 1  # 构造1-10的均匀分布
#         a = rand7()
#         b = rand7()
#         while a == 7:
#             a = rand7()
#         while b > 5:
#             b = rand7()
#         a = 5 if a % 2 == 0 else 0
#         return a + b


# 845


# class Solution:
#     def longestMountain(self, arr: List[int]) -> int:
#         length = len(arr)
#         res = 0
#         left = 0
#         while left + 2 < length:
#             right = left + 1
#             if arr[left] < arr[left + 1]:
#                 while right + 1 < length and arr[right] < arr[right + 1]:
#                     right += 1
#                 if right + 1 < length and arr[right] > arr[right + 1]:
#                     while right + 1 < length and arr[right] > arr[right + 1]:
#                         right += 1
#                     res = max(res, right - left + 1)
#                 else:
#                     right += 1
#             left = right
#         return res

# 493
"""
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3

"""

import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # def mergesort(left, right, tmp):
        #     if left >= right:
        #         return 0
        #     mid = (left + right) // 2
        #     inv_count = mergesort(left, mid, tmp) + mergesort(mid + 1, right, tmp)
        #     for j in range(mid + 1, right + 1):
        #         for i in range(left, mid + 1):
        #             if nums[i] > nums[j] * 2:
        #                 inv_count += (mid - i + 1)
        #                 break
        #     i, j, pos = left, mid + 1, left
        #     while i <= mid and j <= right:
        #         if nums[i] <= nums[j]:
        #             tmp[pos] = nums[i]
        #             i += 1
        #         else:
        #             tmp[pos] = nums[j]
        #             j += 1
        #         pos += 1
        #     for k in range(i, mid + 1):
        #         tmp[pos] = nums[k]
        #         pos += 1
        #     for k in range(j, right + 1):
        #         tmp[pos] = nums[k]
        #         pos += 1
        #     nums[left:right + 1] = tmp[left:right + 1]
        #     return inv_count
        #
        # length = len(nums)
        # tmp = [0] * length
        # return mergesort(0, length - 1, tmp)
        # ans = 0
        # bst = []
        # for num in nums:
        #     right = 2 * num
        #     idx = bisect.bisect_right(bst, right)
        #     ans += len(bst) - idx
        #     bisect.insort(bst, num)
        # return ans
        # 超时
        res = 0
        bst = []
        for n in nums:
            idx = bisect.bisect_right(bst, n*2)
            res += len(bst) - idx
            bisect.insort_right(bst, n)
        return res


s = Solution()
# print(s.reversePairs([1, 3, 2, 3, 1]))
# print(s.reversePairs([1, 3, 2]))
# print(s.reversePairs([3, 1]))
print(s.reversePairs([2, 4, 3, 5, 1]))
# print(s.reversePairs([5, 1]))
"""
func reversePairs(nums []int) int {
    n := len(nums)
    if n <= 1 {
        return 0
    }

    n1 := append([]int(nil), nums[:n/2]...)
    n2 := append([]int(nil), nums[n/2:]...)
    cnt := reversePairs(n1) + reversePairs(n2) // 递归完毕后，n1 和 n2 均为有序

    // 统计重要翻转对 (i,j) 的数量
    // 由于 n1 和 n2 均为有序，可以用两个指针同时遍历
    j := 0
    for _, v := range n1 {
        for j < len(n2) && v > 2*n2[j] {
            j++
        }
        cnt += j
    }

    // n1 和 n2 归并填入 nums
    p1, p2 := 0, 0
    for i := range nums {
        if p1 < len(n1) && (p2 == len(n2) || n1[p1] <= n2[p2]) {
            nums[i] = n1[p1]
            p1++
        } else {
            nums[i] = n2[p2]
            p2++
        }
    }
    return cnt
}
"""
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

 
class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0
        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1

        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r + 1] = tmp[l:r + 1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)
"""
