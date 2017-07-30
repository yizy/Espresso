# https://leetcode.com/problems/lru-cache

class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = {}
        self.head = ListNode(0, '0')
        self.tail = ListNode(0, '0')
        self.size = 0
        self.capacity = capacity
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self.hash:
            return -1
        
        node = self.remove(key)
        self.add(key, node.val)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            self.remove(key)
        
        self.add(key, value)
        if self.size > self.capacity:
            self.remove(self.tail.prev.key)
        
    def remove(self, key):
        if key not in self.hash:
            return
        
        node = self.hash[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        
        del self.hash[key]
        self.size -= 1
        
        return node
    
    def add(self, key, val):
        if key in self.hash:
            return
        
        node = ListNode(key, val)
        
        node.next = self.head.next
        self.head.next.prev = node
        
        node.prev = self.head
        self.head.next = node
        
        self.hash[key] = node
        self.size += 1
 
    
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
