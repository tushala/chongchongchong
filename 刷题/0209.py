# -*- coding: utf-8 -*-
from typing import *

# 多数元素
"""
如果我们把众数记为 +1，把其他数记为 -1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。

算法

Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：

我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；

我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：

如果 x 与 candidate 相等，那么计数器 count 的值增加 1；

如果 x 与 candidate 不等，那么计数器 count 的值减少 1。

在遍历完成后，candidate 即为整个数组的众数。

我们举一个具体的例子，例如下面的这个数组：


[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
在遍历到数组中的第一个元素以及每个在 | 之后的元素时，candidate 都会因为 count 的值变为 0 而发生改变。最后一次 candidate 的值从 5 变为 7，也就是这个数组中的众数。

Boyer-Moore 算法的正确性较难证明，这里给出一种较为详细的用例子辅助证明的思路，供读者参考：

首先我们根据算法步骤中对 count 的定义，可以发现：在对整个数组进行遍历的过程中，count 的值一定非负。这是因为如果 count 的值为 0，那么在这一轮遍历的开始时刻，我们会将 x 的值赋予 candidate 并在接下来的一步中将 count 的值增加 1。因此 count 的值在遍历的过程中一直保持非负。

那么 count 本身除了计数器之外，还有什么更深层次的意义呢？我们还是以数组


[7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
作为例子，首先写下它在每一步遍历时 candidate 和 count 的值：


nums:      [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
candidate:  7  7  7  7  7  7   5  5   5  5  5  5   7  7  7  7
count:      1  2  1  2  1  0   1  0   1  2  1  0   1  2  3  4
我们再定义一个变量 value，它和真正的众数 maj 绑定。在每一步遍历时，如果当前的数 x 和 maj 相等，那么 value 的值加 1，否则减 1。value 的实际意义即为：到当前的这一步遍历为止，众数出现的次数比非众数多出了多少次。我们将 value 的值也写在下方：


nums:      [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
value:      1  2  1  2  1  0  -1  0  -1 -2 -1  0   1  2  3  4
有没有发现什么？我们将 count 和 value 放在一起：


nums:      [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
count:      1  2  1  2  1  0   1  0   1  2  1  0   1  2  3  4
value:      1  2  1  2  1  0  -1  0  -1 -2 -1  0   1  2  3  4
发现在每一步遍历中，count 和 value 要么相等，要么互为相反数！并且在候选众数 candidate 就是 maj 时，它们相等，candidate 是其它的数时，它们互为相反数！

为什么会有这么奇妙的性质呢？这并不难证明：我们将候选众数 candidate 保持不变的连续的遍历称为「一段」。在同一段中，count 的值是根据 candidate == x 的判断进行加减的。那么如果 candidate 恰好为 maj，那么在这一段中，count 和 value 的变化是同步的；如果 candidate 不为 maj，那么在这一段中 count 和 value 的变化是相反的。因此就有了这样一个奇妙的性质。

这样以来，由于：

我们证明了 count 的值一直为非负，在最后一步遍历结束后也是如此；

由于 value 的值与真正的众数 maj 绑定，并且它表示「众数出现的次数比非众数多出了多少次」，那么在最后一步遍历结束后，value 的值为正数；

在最后一步遍历结束后，count 非负，value 为正数，所以它们不可能互为相反数，只可能相等，即 count == value。因此在最后「一段」中，count 的 value 的变化是同步的，也就是说，candidate 中存储的候选众数就是真正的众数 maj。


"""

# 学习了。。。
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         candidate = None
#         for num in nums:
#             if count == 0:
#                 candidate = num
#
#             count += (1 if num == candidate else -1)
#         return candidate

# 992. K 个不同整数的子数组

# from collections import Counter
#
#
# class Solution:
#     def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
#         left, right = 0, 0
#         length = len(A)
#         d = Counter()
#         res = 0
#         while right < length:
#             d[A[right]] += 1
#             while len(d) == K:
#                 tr = right
#                 while tr < length and A[tr] in d:
#                     res += 1
#                     tr += 1
#                 if d[A[left]] == 1:
#                     d.pop(A[left])
#                 else:
#                     d[A[left]] -= 1
#                 left += 1
#             right += 1
#         return res

# 旋转数组
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
#  
#
# 进阶：
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#  
#
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
"""
该方法基于如下的事实：当我们将数组的元素向右移动 kk 次后，尾部 k\bmod nkmodn 个元素会移动至数组头部，其余元素向后移动 k\bmod nkmodn 个位置。

该方法为数组的翻转：我们可以先将所有元素翻转，这样尾部的 k\bmod nkmodn 个元素就被移至数组头部，然后我们再翻转 [0, k\bmod n-1][0,kmodn−1] 区间的元素和 [k\bmod n, n-1][kmodn,n−1] 区间的元素即能得到最后的答案。

我们以 n=7,k=3 为例进行如下展示

"""


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         if not nums or not k:
#             return
#
#         def reverse(s, e, n):
#             while s < e:
#                 n[s], n[e] = n[e], n[s]
#                 s += 1
#                 e -= 1
#
#         n = len(nums) - 1
#         k = k % len(nums)
#         reverse(0, n - k, nums)
#         print(nums)
#         reverse(n - k + 1, n, nums)
#         print(nums)
#         reverse(0, n, nums)
#         print(nums)
# s = Solution()
# s.rotate(nums = [1,2,3,4,5,6,7], k = 3)

# 移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for idx, n in enumerate(nums):
            if n != 0:
                nums[idx], nums[zero] = nums[zero], nums[idx]
                zero += 1

