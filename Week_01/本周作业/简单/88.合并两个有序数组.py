#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 方法1
        # if nums2:
        #     nums1[-n:] = nums2[:]
        #     nums1.sort()

        # # 方法2
        # nums = nums1[:m]
        # p1, p2 = 0, 0
        # idx = 0
        # while p1 < m and p2 < n:
        #     if nums[p1] < nums2[p2]:
        #         nums1[idx] = nums[p1]
        #         p1 += 1
        #     else:
        #         nums1[idx] = nums2[p2]
        #         p2 += 1
        #     idx += 1
        
        # if p1 < m:
        #     nums1[p1+p2: ] = nums[p1:]
        # if p2 < n:
        #     nums1[p1+p2: ] = nums2[p2:]

        # 方法3
        p1, p2 = m-1, n-1
        idx = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
            idx -= 1

        nums1[: p2+1] = nums2[: p2+1]
# @lc code=end

