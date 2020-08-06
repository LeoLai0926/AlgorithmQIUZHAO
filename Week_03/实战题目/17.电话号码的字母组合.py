#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        keyboard = {1: [], 
                    2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 
                    4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 
                    6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 
                    8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

        def helper(index, maxlen, cur):
            if index == maxlen+1:
                res.append(cur)
                return
            
            for letter in keyboard[int(digits[index])]:
                helper(index+1, maxlen, cur+letter)

        cur = ''
        res = []
        helper(0, len(digits)-1, cur)
        return res
# @lc code=end

