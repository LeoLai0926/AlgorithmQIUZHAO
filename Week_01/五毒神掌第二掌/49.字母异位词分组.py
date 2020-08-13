#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for s in strs:
            idn = tuple(sorted(s))
            if idn in cache:
                cache[idn].append(s)
            else:
                cache[idn] = [s]
        return list(cache.values())
# @lc code=end

