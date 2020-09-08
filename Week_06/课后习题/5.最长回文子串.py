#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not n: return ''
        start, end = 0, 0
        for i in range(n):
            l1, r1 = self._expand(s, i, i)
            l2, r2 = self._expand(s, i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start: end+1]
    
    def _expand(self, s, left, right):
        while left >= 0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
# @lc code=end

