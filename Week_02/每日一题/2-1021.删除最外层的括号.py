#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        # 栈
        stack = []
        res = []
        for ch in S:
            if ch == '(':
                stack.append(ch)
                if len(stack) > 1:
                    res.append(ch)
            else:
                stack.pop()
                if len(stack) != 0:
                    res.append(ch)
        return ''.join(res)


# @lc code=end

