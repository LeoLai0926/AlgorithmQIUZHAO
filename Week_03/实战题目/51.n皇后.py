#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.left = set()
        self.right = set()
        self.col = set()

        self.dfs(0, n, [])
        self._generate_result(n)
        return self.res

    def dfs(self, row, n, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return 

        for col in range(n):
            # Terminator
            if col in self.col or row + col in self.right or row - col in self.left:
                # queen died
                continue

            # Process current logic
            # place a queen here
            self.col.add(col)
            self.right.add(row + col)
            self.left.add(row - col)

            self.dfs(row + 1, n, cur_state + [col])

            # Reverse the state
            self.col.remove(col)
            self.right.remove(row + col)
            self.left.remove(row - col)

    def _generate_result(self, n):
        self.res = []
        for board in self.result:
            tmp = []
            for col in board:
                tmp.append('.' * col + 'Q' + '.' * (n - col - 1))
            self.res.append(tmp)




# @lc code=end

