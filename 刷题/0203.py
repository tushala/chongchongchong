# -*- coding: utf-8 -*-
from typing import *


# leetcode-124:二叉树中的最大路径和


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#
#     def maxPathSum(self, root: TreeNode) -> int:
#         import sys
#         res = -sys.maxsize
#
#         def dfs(r: TreeNode):
#             nonlocal res
#             if not r:
#                 return 0
#             left = max(dfs(r.left), 0)
#             right = max(dfs(r.right), 0)
#             cur = r.val + left + right
#             res = max(res, cur)
#             return r.val + max(left, right)
#
#         dfs(root)
#         return res

# 147. 对链表进行插入排序 # todo
# 输入: 4->2->1->3
# 输出: 1->2->3->4
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        ls = head
        curr = head.next
        while curr:
            if ls.val <= curr.val:
                ls = ls.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                ls.next = curr.next
                curr.next = prev.next

# s = Solution()
# l1 = ListNode(4)
# l2 = ListNode(3)
# l3 = ListNode(2)
# l4 = ListNode(1)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# print(s.insertionSortList(l1))

# 200. 岛屿数量

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         length, width = len(grid[0]), len(grid)
#         res = 0
#         dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         def dfs(grid, i, j):
#             if i >= width or i < 0 or j >= length or j < 0:
#                 return
#             if grid[i][j] == "0":
#                 return
#             grid[i][j] = "0"
#             for x, y in dir:
#                 ix, iy = i + x, j + y
#                 dfs(grid, ix, iy)
#
#         for i in range(width):
#             for j in range(length):
#                 if grid[i][j] == "1":
#                     res += 1
#                     dfs(grid, i, j)
#
#         return res

# 529. 扫雷游戏
# class Solution:
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         if board[click[0]][click[1]] == 'M':
#             board[click[0]][click[1]] = 'X'
#             return board
#         else:
#             dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#             length, width = len(board[0]), len(board)
# 
#             def dfs(board, i, j):
#                 if i >= width or i < 0 or j >= length or j < 0:
#                     return
#                 if board[i][j] != 'E':
#                     return
#                 count = 0
#                 for x, y in dirs:
#                     ix = i + x
#                     iy = j + y
#                     if width > ix >= 0 and length > iy >= 0 and board[ix][iy] == 'M':
#                         count += 1
#                 if count == 0:
#                     board[i][j] = 'B'
#                     for x, y in dirs:
#                         ix = i + x
#                         iy = j + y
#                         dfs(board, ix, iy)
#                 else:
#                     board[i][j] = str(count)
# 
#             dfs(board, click[0], click[1])
#             return board
"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(r: TreeNode, minx, maxx):
            return r is None or (minx < r.val < maxx and dfs(r.left, minx, r.val) and dfs(r.right, r.val, maxx))

        return dfs(root, -float("inf"), float("inf"))
