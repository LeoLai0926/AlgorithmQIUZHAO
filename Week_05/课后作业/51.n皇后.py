#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.left = set()
        self.right = set()
        self.col = set()

        self.dfs(0, n, [])
        self._generate_result(n)
        return self.result

    def dfs(self, row, n, cur):
        if row >= n:
            self.res.append(cur)
        
        for col in range(n):
            if col in self.col or \
                row + col in self.right or \
                row - col in self.left:
                continue

            self.col.add(col)
            self.right.add(row + col)
            self.left.add(row - col)

            self.dfs(row + 1, n, cur + [col])

            self.col.remove(col)
            self.right.remove(row + col)
            self.left.remove(row - col)
    
    def _generate_result(self, n):
        self.result = []
        for solution in self.res:
            tmp = []
            for col in solution:
                tmp.append('.'* col + 'Q' + '.' * (n-col-1))
            self.result.append(tmp)


# @lc code=end

