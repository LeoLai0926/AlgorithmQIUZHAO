#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class ListNode:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self._move_node_to_head(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            self._move_node_to_head(key)
        else:
            if len(self.hashmap) == self.capacity:
                self._poptail()
            self._add_node_to_head(key, value)

    def _move_node_to_head(self, key):
        node = self.hashmap[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _add_node_to_head(self, key, value):
        node = ListNode(key, value)
        self.hashmap[key] = node

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _poptail(self):
        node = self.tail.prev
        self.hashmap.pop(node.key)
        node.prev.next = self.tail
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

