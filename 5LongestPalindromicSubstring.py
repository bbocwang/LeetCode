class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        dp = [([False]*len(s))for i in range(len(s))]
        res = ''
        maxlen = 0
        for j in range(len(s)):
            for i in range(j+1):
                dp[i][j] = s[i]==s[j] and ((j-i<=2) or (dp[i+1][j-1]))
                
                if dp[i][j]:
                    if j-i+1 > maxlen:
                        maxlen = j-i+1
                        res = s[i:j+1]
        return res
