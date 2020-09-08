#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = collections.Counter(arr1)
        idx = 0
        for i in range(len(arr2)):
            for j in range(cnt[arr2[i]]):
                arr1[idx+j] = arr2[i]
            idx += cnt[arr2[i]]
            cnt.pop(arr2[i])
        cnt = sorted(cnt.items(), key=lambda x:x[0])
        for i in range(len(cnt)):
            for j in range(cnt[i][1]):
                arr1[idx+j] = cnt[i][0]
            idx += cnt[i][1]
        return arr1
        
# @lc code=end

