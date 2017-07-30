# https://leetcode.com/problems/trapping-rain-water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        i, area = 0, 0
        while i < len(height):
            if not stack or height[stack[-1]] >= height[i]:
                stack.append(i)
                i += 1
            else:
                bottom = height[stack.pop()]
                if stack:
                    area += (min(height[stack[-1]], height[i]) - bottom) * (i - stack[-1] - 1)
        return area
