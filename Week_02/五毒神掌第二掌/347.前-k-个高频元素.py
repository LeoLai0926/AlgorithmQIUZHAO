#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
        
        cache_sort = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in cache_sort[:k]]



# @lc code=end

