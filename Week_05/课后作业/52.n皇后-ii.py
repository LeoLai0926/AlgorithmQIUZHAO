#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    # def totalNQueens(self, n: int) -> int:
    #     self.res = 0
    #     self.left = set()
    #     self.right = set()
    #     self.col = set()

    #     self.dfs(n, 0)
    #     return self.res

    # def dfs(self, n, row):
    #     if row >= n:
    #         self.res += 1
    #         return
        
    #     for col in range(n):
    #         if col in self.col or \
    #             (row+col) in self.left or \
    #             (row-col) in self.right:
    #             continue

    #         self.col.add(col)
    #         self.left.add(row+col)
    #         self.right.add(row-col)
            
    #         self.dfs(n, row+1)

    #         self.col.remove(col)
    #         self.left.remove(row+col)
    #         self.right.remove(row-col)
        
    def totalNQueens(self, n):
        if n < 1: return []
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, col, right, left):
        if row >= n:
            self.count += 1
            return 

        # 获取当前所有的空位
        bits = (~(col | right | left)) & ((1 << n) - 1)

        while bits:
            # 获取最低位的 1
            p = bits & -bits
            # 在 p 这个位置放上皇后
            bits = bits & (bits - 1)
            self.dfs(n, row+1, col | p , (right | p) << 1, (left | p) >> 1)



# @lc code=end

