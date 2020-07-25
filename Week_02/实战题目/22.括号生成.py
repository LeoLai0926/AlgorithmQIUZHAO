#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        
        # 递归
        res = []

        def helper(cur, left, right, n):
            if left == n and right == n:
                res.append(cur)
                return 

            if left < n:
                helper(cur+'(', left+1, right, n)
            if right < left:
                helper(cur+')', left, right+1, n)

        helper('', 0, 0, n)
        return res


# @lc code=end

