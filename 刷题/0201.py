# -*- coding: utf-8 -*-
# 82. 删除排序链表中的重复元素 II

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#         res = ListNode(0)
#         x = res
#         if head and head.next and head.val == head.next.val:
#             while head and head.next and head.val == head.next.val:
#                 head = head.next
#         else:
#             res.next = ListNode(head.val)
#             res = res.next
#         res.next = self.deleteDuplicates(head.next)
#         return x.next



# 19. 删除链表的倒数第 N 个结点
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         fast = head
#         for i in range(n):
#             fast = fast.next
#         if not fast:
#             return head.next
#         slow = head
#         while fast.next:
#             fast = fast.next
#             slow = slow.next
#
#         slow.next = slow.next.next
#         return head

# 83. 删除排序链表中的重复元素
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         p = head
#         while p and p.next:
#             if p.val == p.next.val:
#                 p.next = p.next.next
#             else:
#                 p = p.next
#         return head

# 445. 两数相加 II

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         stack1 = []
#         stack2 = []
#         t1, t2 = l1, l2
#         while t1:
#             stack1.append(t1.val)
#             t1 = t1.next
#
#         while t2:
#             stack2.append(t2.val)
#             t2 = t2.next
#
#         carry = 0
#         res = None
#         while stack1 or stack2 or carry:
#             v1 = stack1.pop() if stack1 else 0
#             v2 = stack2.pop() if stack2 else 0
#             val = (v1 + v2 + carry) % 10
#             carry = (v1 + v2 + carry) // 10
#             node = ListNode(val)
#             node.next = res
#             res = node
#         return res
