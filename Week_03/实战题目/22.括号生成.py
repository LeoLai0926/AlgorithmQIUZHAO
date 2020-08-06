#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # # DFS
        # res = []
        # cur = ''

        # def dfs(left, right, maxlen, cur):
        #     # Terminator
        #     if left == n and right == n:
        #         res.append(cur)
        #         return 

        #     # Process current logic
        #     if left < n:
        #         dfs(left + 1, right, maxlen, cur + '(')
        #     if right < left:
        #         dfs(left, right + 1, maxlen, cur + ')')
            
        # dfs(0, 0, n, cur)
        # return res

        # BFS
        queue = collections.deque()
        queue.append(('', 0, 0))
        res = []

        while queue:
            cur, left, right = queue.popleft()
            # Terminator
            if left == n and right == n:
                res.append(cur)

            # Process current logic
            if left < n:
                queue.append((cur+'(', left + 1, right))
            if right < left:
                queue.append((cur+')', left, right + 1))

        return res

            


# @lc code=end

