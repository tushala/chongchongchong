# -*- coding: utf-8 -*- 
"""
403. 青蛙过河
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。



示例 1：

输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
示例 2：

输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

"""


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        ...


# 297


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# from collections import deque
#
#
# class Codec:
#     tag = 'n'
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return ""
#         res = ""
#         queue = deque()
#         queue.append(root)
#         while queue:
#             root = queue.popleft()
#             if root:
#                 res += str(root.val)
#                 queue.append(root.left)
#                 queue.append(root.right)
#             else:
#                 res += self.tag
#             res += " "
#         return res
#
#     def deserialize(self, data):
#         if not data:
#             return None
#         tree = data.split()
#         if tree[0] == self.tag:
#             return None
#         queue = deque()
#
#         root = TreeNode(int(tree[0]))
#         queue.append(root)
#         i = 1
#         while queue:
#             cur = queue.popleft()
#             if cur is None:
#                 continue
#             cur.left = TreeNode(int(tree[i])) if tree[i] != 'n' else None
#             cur.right = TreeNode(int(tree[i+1])) if tree[i+1] != 'n' else None
#             i += 2
#             queue.append(cur.left)
#             queue.append(cur.right)
#
#         return root


# 147
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        lnode = head
        cur = head.next
        while cur:
            if cur.val >= lnode.val:
                lnode = lnode.next
            else:
                d = dummy
                while d.next.val <= cur.val:
                    d = d.next
                lnode.next = cur.next
                cur.next = d.next
                d.next = cur
                
            cur = lnode.next
        return dummy.next