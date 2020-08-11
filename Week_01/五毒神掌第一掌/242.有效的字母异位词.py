#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = [0 for _ in range(26)]
        for ch in s:
            idx = ord(ch) - ord('a')
            cache[idx] -= 1
        for ch in t:
            idx = ord(ch) - ord('a')
            cache[idx] += 1
        for flag in cache:
            if flag != 0:
                return False
        return True
# @lc code=end

