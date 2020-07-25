#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        d = collections.deque()
        d.append(root)
        res = []
        while d:
            cur = d.popleft()
            if cur:
                res.append(str(cur.val))
                d.append(cur.left)
                d.append(cur.right)
            else:
                res.append('X')
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """        
        if not data: return None
        data = data.split(',')[::-1]
        root = TreeNode(data.pop())
        d = collections.deque([root])
        while d:
            cur = d.popleft()
            if data:
                val = data.pop()
                if val != 'X':
                    cur.left = TreeNode(val)
                    d.append(cur.left)
            if data:
                val = data.pop()
                if val != 'X':
                    cur.right = TreeNode(val)
                    d.append(cur.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

