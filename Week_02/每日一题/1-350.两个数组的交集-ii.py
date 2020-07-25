#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # 方法1
        # res = []
        # while nums1 and nums2:
        #     n = nums1.pop()
        #     if n in nums2:
        #         nums2.remove(n)
        #         res.append(n)
        #     else:
        #         continue
        # return res

        # # 哈希
        # n1 = len(nums1)
        # n2 = len(nums2)
        # if n1 > n2:
        #     self.intersect(nums2, nums1)

        # count1 = {}
        # for n in nums1:
        #     if n in count1:
        #         count1[n] += 1
        #     else:
        #         count1[n] = 1
        
        # count2 = {}
        # for n in nums2:
        #     if n not in count1:
        #         continue
        #     else:
        #         if n in count2:
        #             count2[n] += 1
        #         else:
        #             count2[n] = 1
        
        # res = []
        # for key in count2.keys():
        #     times = min(count1[key], count2[key])
        #     for _ in range(times):
        #         res.append(key)
        # return res

        # Python 大法好
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        return num.elements()

# @lc code=end

