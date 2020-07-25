# [剑指 Offer 40]. 最小的k个数

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        # Python 自带模块
        import heapq
        heapq.heapify(arr)
        res =  []
        for _ in range(k):
            res.append(heapq.heappop(arr))
        return res
