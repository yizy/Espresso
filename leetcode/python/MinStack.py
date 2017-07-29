# https://leetcode.com/problems/min-stack

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            self.mins.append(min(self.mins[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        if self.nums:
            self.nums.pop()
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
