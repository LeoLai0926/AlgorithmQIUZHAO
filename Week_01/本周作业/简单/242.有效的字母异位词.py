#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False
        n = len(s)
        index = [0] * 26
        for i in range(n):
            index[ord(s[i]) - ord('a')] += 1
            index[ord(t[i]) - ord('a')] -= 1
        
        for i in index:
            if i != 0: return False
        return True

# @lc code=end

