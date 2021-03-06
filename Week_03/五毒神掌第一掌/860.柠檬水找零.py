#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for pay in bills:
            if pay == 5:
                five += 1
            elif pay == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if not five and not ten: return False
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3: 
                    five -= 3
                else:
                    return False
        return True
        
# @lc code=end

