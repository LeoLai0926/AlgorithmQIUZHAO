#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = collections.deque()
        queue.append((start, 0))
        bankset = set(bank)

        while queue:
            cur, step = queue.popleft()
            # Terminator
            if cur == end: return step

            # Process current logic
            for i in range(len(cur)):
                for c in 'AGTC':
                    mutation = cur[:i] + c + cur[i+1:]
                    if mutation in bankset:
                        queue.append((mutation, step + 1))
                        bankset.remove(mutation)

        return -1

        
# @lc code=end

