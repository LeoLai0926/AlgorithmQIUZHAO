#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # 哈希+排序
        # cnt = dict()
        # for i, n in enumerate(nums):
        #     if n in cnt:
        #         cnt[n] += 1
        #     else:
        #         cnt[n] = 1
        # res = sorted(cnt.keys(), key=cnt.get, reverse=True)
        # return res[:k]

        # 哈希+大根堆
        cnt = dict()
        for i, n in enumerate(nums):
            if n in cnt:
                cnt[n] += 1
            else:
                cnt[n] = 1

        res = heapq.nlargest(k, cnt.keys(), key=cnt.get)
        return res



# @lc code=end

