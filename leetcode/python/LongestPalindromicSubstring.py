# https://leetcode.com/problems/longest-palindromic-substring

# DFS + Memo, but TLE
class SolutionDFSMemo(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def dfs(s, i, j, memo):
            if i == j or i + 1 == j and s[i] == s[j]:
                return True
            
            if (i, j) not in memo:
                memo[(i, j)] = s[i] == s[j] and dfs(s, i + 1, j - 1, memo)
            
            return memo[(i, j)]
        
        memo, p = {}, ""
        for j in range(len(s)):
            for i in range(j+1):
                if dfs(s, i, j, memo) and j - i + 1 > len(p):
                    p = s[i:j+1]
        return p
        
class SolutionDP(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = ""
        memo = [[None] * len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j+1):
                if not memo[i][j]:
                    memo[i][j] = i == j or s[i] == s[j] and (i + 1 == j or memo[i+1][j-1])
                    
                    if memo[i][j] and j - i + 1 > len(p):
                        p = s[i:j+1]
        return p
