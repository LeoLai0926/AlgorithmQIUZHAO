#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        (row, col) = click
        m, n = len(board), len(board[0])
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), 
                      (-1, -1), (-1, 1), (1, -1), (1, 1))
        if 0 <= row < m and 0 <= col < n:
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row+r][col+c] == "M" 
                        for r, c in directions
                        if 0 <= row+r < m and 0 <= col+c < n])
                board[row][col] = str(n or "B")
                if not n:
                    for r, c in directions:
                        self.updateBoard(board, [row+r, col+c])

        return board        

# @lc code=end

