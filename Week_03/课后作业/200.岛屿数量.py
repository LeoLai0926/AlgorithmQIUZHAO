#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # # DFS
        # def dfsmarking(i, j):
        #     if  i < 0 or i >= m or \
        #         j < 0 or j >= n or \
        #         grid[i][j] == "0":
        #         return 
        #     grid[i][j] = "0"
        #     dfsmarking(i-1, j)
        #     dfsmarking(i+1, j)
        #     dfsmarking(i, j-1)
        #     dfsmarking(i, j+1)

        # res = 0
        # if not grid: return res
        # m, n = len(grid), len(grid[0])

        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] == "1":
        #             res += 1
        #             dfsmarking(row, col)

        # return res

        # BFS
        res = 0
        if not grid: return res
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0":
                    continue

                queue = collections.deque()
                queue.append((row, col))

                while queue:
                    i, j = queue.popleft()
                    for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if ni < 0 or ni >= m or \
                            nj < 0 or nj >= n or \
                            grid[ni][nj] == "0":
                            continue
                        queue.append((ni, nj))
                        grid[ni][nj] = "0"
                
                res += 1
        return res

            

# @lc code=end

