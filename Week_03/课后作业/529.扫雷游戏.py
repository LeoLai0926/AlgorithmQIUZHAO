#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        (row, col) = click
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == "M":
                board[row][col] = "X"
            elif board[row][col] == "E":
                n = sum([board[row+r][col+c] == "M" for r, c in directions if 0 <= row+r < len(board) and 0 <= col+c < len(board[0])])
                board[row][col] = str(n or "B")
                for r, c in directions:
                    if not n:
                        self.updateBoard(board, [row + r, col + c])
        return board

        
# @lc code=end

