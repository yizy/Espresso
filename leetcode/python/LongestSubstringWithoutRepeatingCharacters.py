# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = max_len = 0
        visited = set()
        for r in range(len(s)):
            if s[r] in visited:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1
            else:
                visited.add(s[r])
            
            max_len = max(max_len, r - l + 1)
        
        return max_len
