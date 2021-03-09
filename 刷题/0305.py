# -*- coding: utf-8 -*- 


# 面试题 08.11.
# class Solution:
#     def waysToChange(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         dp[0] = 1
#         for j in [1, 5, 10, 25]:
#             for i in range(j, n+1):
#                 dp[i] += dp[i - j]
#         return dp[-1] % (10 ** 9 + 7)

# 2. 两数相加
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         p = res = ListNode(0)
#         carry = 0
#         while l1 or l2:
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             v = x + y + carry
#             carry = v // 10
#             v = v % 10
#             res.next = ListNode(v)
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#             res = res.next
#         if carry:
#             res.next = ListNode(1)
#         return p.next

# 有效的数独
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         lows, columns, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
#         for low in range(9):
#             for col in range(9):
#                 if board[low][col].isdigit():  # 或者用 board[low][col] != '.'也可以
#                     # *  # 以下三个if判断是不是在行、列和 3*3宫格内存在有重复数字*
#                     if board[low][col] in lows[low]:
#                         return False
#                     if board[low][col] in columns[col]:
#                         return False
#                     # *  # 这里3*3宫格缩小1/3*
#                     if board[low][col] in boxes[low // 3, col // 3]:
#                         return False
#                     # *  # 没存在加入行、列和 3*3宫格*
#                     lows[low].add(board[low][col])
#                     columns[col].add(board[low][col])
#                     boxes[low // 3, col // 3].add(board[low][col])
#
#         return True

# 1出现的次数
class Solution:

    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [[-1] * 20 for _ in range(20)]
        num = [0] * 20

        def dfs(pos, count, limit):
            if not pos:
                return count
            if not lim and dp[pos][count] != -1:
                return dp[pos][count]
            res = 0
            ub = num[pos] if limit else 9
            for i in range(ub + 1):
                res += dfs(pos - 1, count + (i == 1), limit & num[pos])
            if not limit:
                dp[pos][count] = res
            return res

        def cal(x):
            cnt = 0
            while x:
                cnt += 1
                num[cnt] = x % 10
                x /= 10
            return dfs(cnt - 1, 0, 1)

        return cal(n)

    s = Solution()
