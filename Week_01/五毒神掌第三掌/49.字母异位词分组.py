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
            idx = tuple(sorted(s))
            if idx not in cache:
                cache[idx] = [s]
            else:
                cache[idx].append(s)
        return list(cache.values())
# @lc code=end

