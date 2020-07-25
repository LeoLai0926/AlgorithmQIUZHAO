#
# @lc app=leetcode.cn id=239 lang=python3
#
# 剑指 Offer 59 - I. 滑动窗口的最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列
        d = collections.deque()
        res = []

        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(i)

            if d[0] == i-k:
                d.popleft()

            if i>=k-1:
                res.append(nums[d[0]])
        return res

# @lc code=end

