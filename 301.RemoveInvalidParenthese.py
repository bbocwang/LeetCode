class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.l = 0
        self.r = 0
        self.getLR(s)
        L=self.l
        R = self.r
        ans = []
        dfs(s,0,L,R,ans)
        return ans
        
        
    def dfs(self,s,start,l,r,ans):
        if l == 0 and r == 0:
            if self(isValid(s)):
                ans.append(s)
                return
        for i in range(start,len(s)):
            if s[i] == s[i-1] and i != start:
                continue
            elif s[i] == ')' and r > 0:
                curr = removeChar(s,i)
                r -= 1
                dfs(curr,i,l,r,ans)
            el
                
    def removeChar(self,s.i):
        head = s[:n]
        tail = s[n+1:]
        return head+tail
        
        
    
    
    def getLR(self,s):
        
        for i in s:
            if i == '(':
                self.l += 1
            elif i == ')':
                if self.l > 0:
                    self.l -= 1
                elif self.l == 0:
                    self.r += 1
    def isValid(self,s):
        l=0
        r=0
        for i in s:
            if i == '(':
                l += 1
            elif i == ')':
                r += 1
                if r > l:
                    return False
        if l == r:
            return True
        else:
            return False
        
