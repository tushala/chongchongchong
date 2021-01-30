# -*- coding: utf-8 -*-
from typing import *

# 160
"""

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点


intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。


"""
"""
创建两个指针 pApA 和 pBpB，分别初始化为链表 A 和 B 的头结点。然后让它们向后逐结点遍历。
当 pApA 到达链表的尾部时，将它重定位到链表 B 的头结点 (你没看错，就是链表 B); 类似的，当 pBpB 到达链表的尾部时，将它重定位到链表 A 的头结点。
若在某一时刻 pApA 和 pBpB 相遇，则 pApA/pBpB 为相交结点。
想弄清楚为什么这样可行, 可以考虑以下两个链表: A={1,3,5,7,9,11} 和 B={2,4,9,11}，相交于结点 9。 由于 B.length (=4) < A.length (=6)，pBpB 比 pApA 少经过 22 个结点，会先到达尾部。将 pBpB 重定向到 A 的头结点，pApA 重定向到 B 的头结点后，pBpB 要比 pApA 多走 2 个结点。因此，它们会同时到达交点。
如果两个链表存在相交，它们末尾的结点必然相同。因此当 pApA/pBpB 到达链表结尾时，记录下链表 A/B 对应的元素。若最后元素不相同，则两个链表不相交。
复杂度分析


"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if headA is None or headB is None:
#             return None
#         ha = headA
#         hb = headB
#         while ha != hb:
#             ha = ha.next if ha else headB
#             hb = hb.next if hb else headA
#         return ha
# 买卖股票的最佳时机
"""
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

"""

#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         pre = prices[0]
#         res = 0
#         for i in range(1, len(prices)):
#             pre = min(pre, prices[i])
#             res = max(res, prices[i]-pre)
#         return res

# 508
"""
给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

 

示例 1：
输入:

  5
 /  \
2   -3
返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。

示例 2：
输入：

  5
 /  \
2   -5
返回 [2]，只有 2 出现两次，-5 只出现 1 次。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-frequent-subtree-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# from collections import Counter
#
#
# class Solution:
#     def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
#         def get_sum_list(root):
#             if not root:
#                 return []
#             if not root.left and not root.right:
#                 return [root.val]
#             else:
#                 res = []
#                 lres = get_sum_list(root.left)
#                 rres = get_sum_list(root.right)
#                 if lres and rres:
#                     res.extend(lres)
#                     res.extend(rres)
#                     res.append(root.val + lres[-1] + rres[-1])
#                 elif lres:
#                     res.extend(lres)
#                     res.append(root.val + lres[-1])
#                 elif rres:
#                     res.extend(rres)
#                     res.append(root.val + rres[-1])
#                 else:
#                     res.append(root.val)
#                 return res
#
#         if not root:
#             return []
#         c = Counter(get_sum_list(root))
#         m = c.most_common(1)[0][1]
#         res = []
#         for k in c:
#             if c[k] == m:
#                 res.append(k)
#         return res

