#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList: return 0
        queue = collections.deque()
        queue.append((beginWord, 1))
        visited =set()
        visited.add(beginWord)
        wordList = set(wordList)
        candidate = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            curWord, dist = queue.popleft()
            visited.add(curWord)
            if curWord == endWord: return dist

            for i in range(len(curWord)):
                for j in candidate:
                    tmpWord = curWord[:i] + j + curWord[i+1:]
                    if tmpWord not in visited and tmpWord in wordList:
                        queue.append((tmpWord, dist + 1))
                        visited.add(tmpWord)
        return 0
        
# @lc code=end

