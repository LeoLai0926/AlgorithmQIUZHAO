#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        i = 0
        while i < n:
            i += 1
            cur = heapq.heappop(heap)
            for fac in [2, 3, 5]:
                if cur * fac not in heap:
                    heapq.heappush(heap, cur * fac)
        return cur
                


# @lc code=end

