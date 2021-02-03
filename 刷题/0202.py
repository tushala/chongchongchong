# -*- coding: utf-8 -*-
from typing import *


# 剑指 Offer 35. 复杂链表的复制  没看懂？？？
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':

# 110. 平衡二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         def height(r: TreeNode):
#             if not r:
#                 return 0
#             if r and not r.left and not r.right:
#                 return 1
#             return max(height(r.left), height(r.right)) + 1
#         if not root:
#             return True
#         return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# 剑指 Offer 07. 重建二叉树
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         r = preorder[0]
#         idx = inorder.index(r)
#         t = TreeNode(r)
#         t.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
#         t.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
#         return t
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]


# 剑指 Offer 32 - I. 从上到下打印二叉树

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         res = []
#         curlayer = [root]
#         while curlayer:
#             nxtlayer = []
#             for c in curlayer:
#                 res.append(c.val)
#                 if c.left:
#                     nxtlayer.append(c.left)
#                 if c.right:
#                     nxtlayer.append(c.right)
#
#             curlayer = nxtlayer
#         return res

# 剑指 Offer 32 - III. 从上到下打印二叉树 III


# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         curlayer = [root]
#         n = 0
#         while curlayer:
#             nxtlayer = []
#             _res = []
#             for c in curlayer:
#                 _res.append(c.val)
#                 if c.left:
#                     nxtlayer.append(c.left)
#                 if c.right:
#                     nxtlayer.append(c.right)
#             if not n % 2:
#                 _res = _res[::-1]
#             res.append(_res)
#             curlayer = nxtlayer
#         return res
# 剑指 Offer 34. 二叉树中和为某一值的路径
# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         res = []
#
#         def get_path(r, target, ans):
#             nonlocal res
#             if r and not r.left and not r.right:
#                 if target == r.val:
#                     return res.append(list(ans + (r.val,)))
#             else:
#                 if r.left:
#                     get_path(r.left, target - r.val, ans + (r.val,))
#                 if r.right:
#                     get_path(r.right, target - r.val, ans + (r.val,))
#         if not root:
#             return []
#         get_path(root, sum, ())
#         return res

# 337. 打家劫舍 III
# 在上次打劫完一条街道之后和一圈房屋后，
# 小偷又发现了一个新的可行窃的地区。
# 这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
# 一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
from functools import lru_cache


class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dfs(r: TreeNode):
            if not r:
                return 0, 0
            ch = r.val + dfs(r.left)[1] + dfs(r.right)[1]
            ns = max(dfs(r.left)) + max(dfs(r.right))
            return ch, ns

        return max(dfs(root))
