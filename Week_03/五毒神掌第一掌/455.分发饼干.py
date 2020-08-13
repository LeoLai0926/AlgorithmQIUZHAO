#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pg, ps = 0, 0
        while pg < len(g) and ps < len(s):
            if s[ps] >= g[pg]:
                pg += 1
            ps +=  1
        return pg

# @lc code=end

