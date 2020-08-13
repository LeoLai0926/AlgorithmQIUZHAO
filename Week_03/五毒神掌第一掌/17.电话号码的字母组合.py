#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cache = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        if not digits: return res
        def helper(idx, maxlen, cur):
            if idx == maxlen: 
                res.append(''.join(cur))
                return
            for ch in cache[digits[idx]]:
                helper(idx + 1, maxlen, cur + [ch])
            
        helper(0, len(digits), [])
        return res
# @lc code=end

