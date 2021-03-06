#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumb = ListNode(0)
        res = dumb
        while l1 and l2:
            if l1.val <= l2.val:
                dumb.next = l1
                l1 = l1.next
            else:
                dumb.next = l2
                l2 = l2.next
            dumb = dumb.next
        
        dumb.next = l1 if l1 else l2
        return res.next



        
# @lc code=end

