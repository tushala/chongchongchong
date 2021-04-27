# -*- coding: utf-8 -*- 
from typing import *
from collections import *
import heapq

# 743
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#
#         graph = defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((w, v))
#
#         dist = {node: float('inf') for node in range(1, n + 1)}
#
#         def dfs(node, elapsed):
#             if elapsed >= dist[node]:
#                 return
#             dist[node] = elapsed
#             for time, nei in sorted(graph[node]):
#                 dfs(nei, elapsed + time)
#
#         dfs(k, 0)
#         ans = max(dist.values())
#         return ans if ans < float('inf') else -1


# 50
"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。

 

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：

输入：x = 2.10000, n = 3
输出：9.26100
示例 3：

输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


"""

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             return 1 / self.myPow(x, -n)
#         res = 1
#         mi = x
#         while n:
#             if n & 1:
#                 res *= mi
#             n = n >> 1
#             mi *= mi
#         return res


# 剑指 Offer 13. 机器人的运动范围

# class Solution:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         vistied = [[0] * n for _ in range(m)]
#
#         def dfs(i, j):
#             if i < 0 or i >= m or j < 0 or j >= n or (i // 10 + i % 10 + j // 10 + j % 10) > k or vistied[i][j]:
#                 return 0
#             vistied[i][j] = 1
#             return dfs(i + 1, j) + dfs(i - 1, +j) + dfs(i, j + 1) + dfs(i, +j - 1) + 1
#
#         return dfs(0, 0)

# 854
"""
如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。

给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。

 

示例 1：

输入：A = "ab", B = "ba"
输出：1
示例 2：

输入：A = "abc", B = "bca"
输出：2
示例 3：

输入：A = "abac", B = "baca"
输出：2
示例 4：

输入：A = "aabc", B = "abca"
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-similar-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""

"""


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        ...


# 剑指 Offer 49.
"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n
        a, b, c = 0, 0, 0
        e, s, w = 1, 1, 1
        i = 0
        while i != n:
            mi = min(e, s, w)
            if e == mi:
                e *= 2
            elif s == mi:
                s *= 2
            else:
                w *= 2
            i += 1
        return mi

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        idx_a = 0
        idx_b = 0
        idx_c = 0
        for i in range(1,n):
            dp[i] = min(dp[idx_a] * 2, dp[idx_b] * 3, dp[idx_c] * 5)
            if dp[i] == dp[idx_a] * 2:
                idx_a += 1
            if dp[i] == dp[idx_b] * 3:
                idx_b += 1
            if dp[i] == dp[idx_c] * 5:
                dp[i] == dp[idx_c] * 5
                idx_c += 1
        return dp[-1]

s = Solution()

print(s.myPow(2.00000, -2))
print(s.myPow(-2.00000, 2))
print(s.myPow(2, 2))
print(s.myPow(2, -2))
