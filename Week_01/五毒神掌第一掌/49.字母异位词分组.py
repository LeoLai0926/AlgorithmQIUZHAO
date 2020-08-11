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
            if tuple(sorted(s)) not in cache:
                cache[tuple(sorted(s))] = [s]
            else:
                cache[tuple(sorted(s))].append(s)
        return list(cache.values())
# @lc code=end

