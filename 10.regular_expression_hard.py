class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [([False]* (len(s)+1)) for _ in range(len(p)+1)]
        dp[0][0] =  True

        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                dp[i][0] = dp[i-2][0]


        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if (p[j-1] == s[i-1] or p[j-1] == '.'):
                    dp[j][i] = dp[j-1][i-1]

                elif p[j-1] == '*' :
                    if (s[i-1]==p[j-2] or p[j-2]=='.'):
                        dp[j][i] =  dp[j][i-1] or dp[j-1][i] or dp[j-2][i]
                    else:
                        dp[j][i] =   dp[j-2][i]

        return dp[len(p)][len(s)]
        






class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        star = False
        mem = ''
        
        for i,k in enumerate(p):
            if  k == '.':
                dot_mem = s[0]
                if i+1 < len(p) and p[i+1] == '*':
                    while s[0] == s[1]:
                        s.replace(s[0],'')
                    s.replace(s[0],'')
                else:
                    s.replace(s[0],'')
            else:
                if i+1 < len(p) and p[i+1] == '*':
                    while s[0] == k and s[0] == s[1]:
                        s.replace(s[0],'')
                    s.replace(s[0],'')
                else:
                    if s[0] == k:
                        s.replace(s[0],'')
                    else:
                        return False
        if len(s) == 0:
            return True
        else :return False
        
        
        
        
        
        if not p: return not s
        
        first_match = bool(s) and ( p[0] in {s[0],'.'})
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s,p[2:]) or (first_match and self.isMatch(s[1:],p[2:]))
        else:
            return first_match and self.isMatch(s[1:],p[1:])
