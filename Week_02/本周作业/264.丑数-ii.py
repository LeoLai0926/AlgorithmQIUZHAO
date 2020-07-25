#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        factor = [2, 3, 5]
        heap = [1]
        heapq.heapify(heap)
        i = 0
        while len(heap) > 0:
            res = heapq.heappop(heap)
            i += 1
            if i >= n: return res
            for fac in factor:
                if fac * res not in heap:
                    heapq.heappush(heap, fac * res)
        return -1
        
# @lc code=end

