# -*- coding: utf-8 -*-
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 994. 腐烂的橘子

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]
#         length, width = len(grid[0]), len(grid)
#         olist = []
#         for i in range(width):
#             for j in range(length):
#                 if grid[i][j] == 2:
#                     olist.append([i, j])
#         res = 0
#         while olist:
# 
#             nxtolist = []
#             for i, j in olist:
#                 for x, y in dir:
#                     nx, ny = i + x, j + y
#                     if 0 <= nx < width and 0 <= ny < length and grid[nx][ny] == 1:
#                         grid[nx][ny] = 2
#                         nxtolist.append([nx, ny])
#             olist = nxtolist
#             if not olist:
#                 break
#             res += 1
#         for i in range(width):
#             for j in range(length):
#                 if grid[i][j] == 1:
#                     return -1
#         return res


# 199. 二叉树的右视图


# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         cur_layer = [root]
#         res = []
#         while cur_layer:
#             res.append(cur_layer[-1].val)
#             nxt_layer = []
#             for node in cur_layer:
#                 if node.left:
#                     nxt_layer.append(node.left)
#                 if node.right:
#                     nxt_layer.append(node.right)
#             cur_layer = nxt_layer
#         return res

# 112. 路径总和
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root:
#             return False
#         def dfs(root, sum):
#             if not root.left and not root.right:
#                 return root.val == sum
#             elif not root.left:
#                 return dfs(root.right, sum-root.val)
#             elif not root.right:
#                 return dfs(root.left, sum-root.val)
#             else:
#                 return dfs(root.left, sum - root.val) or dfs(root.right, sum-root.val)
#         return dfs(root, targetSum)


# 143. 重排链表
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         mid = self.getmid(head)
#         l1 = head
#         l2 = mid.next
#         mid.next = None
#         l2 = self.reverse(l2)
#         self.mergeList(l1, l2)
#
#     def mergeList(self, l1, l2):
#         while l1 and l2:
#             nxt1 = l1.next
#             nxt2 = l2.next
#             l1.next = l2
#             l1 = nxt1
#             l2.next = l1
#             l2 = nxt2
#
#     def getmid(self, head: ListNode):
#         if not head:
#             return None
#         slow, fast = head, head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#         mid = slow
#         return mid
#
#     def reverse(self, head: ListNode):
#         pre = None
#         cur = head
#         while cur:
#             nxt = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nxt
#         return pre

# 链表还是菜