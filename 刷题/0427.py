# -*- coding: utf-8 -*- 

# 306


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def pd(start: int, next: int, res: str):
            if not res:
                return True
            s = str(start + next)
            if res.startswith(s):
                return pd(next, int(s), res[len(s):])
            return False

        def strvaild(s):
            return len(s) == 1 or (len(s) > 1 and not s.startswith('0'))

        length = len(num)
        first_cut = length * 2 // 3
        for fc in range(2, first_cut + 1):
            res_num = num[fc:]
            for sc in range(1, fc):
                first, second = num[:sc], num[sc:fc]
                if strvaild(first) and strvaild(second):
                    if pd(int(first), int(second), res_num):
                        return True
        return False


"""
在你的面前从左到右摆放着n根长短不一的木棍，你每次可以折断一根木棍，
并将折断后得到的两根木棍一左一右放在原来的位置
（即若原木棍有左邻居，则两根新木棍必须放在左邻居的右边，若原木棍有右邻居，新木棍必须放在右邻居的左边，所有木棍保持左右排列）。
折断后的两根木棍的长度必须为整数，且它们之和等于折断前的木棍长度。
你希望最终从左到右的木棍长度单调不减，那么你需要折断多少次呢？



示例

输入：[3,5,13,9,12]
输出：1

输入：[3,12,13,9,12]
输出：2

输入：[3,13,12,9,12]
输出：3

输入：[3,13,60,7]
输出：10

输入：[3,63,7]
输出：8

输入：[9,1]
输出：8

"""


def breakNum(nums):
    res = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < nums[i - 1]:
            t = (nums[i - 1] - 1) // nums[i]
            res += t
            nums[i - 1] /= (t + 1)
    return res
