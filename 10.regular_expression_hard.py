class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        #dp array: row: char in pattern
        #          column: char in string
        dp = [([False]* (len(s)+1)) for _ in range(len(p)+1)]
        
        #initial: set the left most top value to be true becaue empty string can be accepted 
        dp[0][0] =  True
        
        #initial fill the left most star entries with the same value of two row up 
        #because the star char can be '' so if it is true two row before, it can be accept as well
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                dp[i][0] = dp[i-2][0]
        

        #if current string is not *, the cell is filled by the value of dp[j-1][i-1]
        #if current string is *,
        #   first: if current char in string is the same to the char in pattern before *:  
        #       fill the cell with the value of:
        #                1: dp[j][i-1] (accepting multiple current string)
        #                or 
        #                2: dp[j-2][i]) (accept the string when * is empty)
        #   secone: if current char is not same to the *char:
        #               simply fill it with accepting the string when *char is empty
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if (p[j-1] == s[i-1] or p[j-1] == '.'):
                    dp[j][i] = dp[j-1][i-1]

                elif p[j-1] == '*' :
                    if (s[i-1]==p[j-2] or p[j-2]=='.'):
                        dp[j][i] =  dp[j][i-1] or dp[j-2][i]
                    else:
                        dp[j][i] =   dp[j-2][i]

        return dp[len(p)][len(s)]  
