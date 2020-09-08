#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        r = []
        while s:
            w = s.pop()
            if w:
                r.append(w)
        return ' '.join(r)
# @lc code=end

