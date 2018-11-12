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
        self.ans = []
        self.dfs(s,0,L,R)
        return self.ans
        
        
    def dfs(self,s,start,l,r):
        if l == 0 and r == 0:

            if self.isValid(s):
                self.ans.append(s)
                return
        for i in range(start,len(s)):
            if s[i] == s[i-1] and i != start:
                continue
            elif s[i] == ')' and r > 0:
                curr = self.removeChar(s,i)
                self.dfs(curr,i,l,r-1)
            elif s[i] == '(':
                curr = self.removeChar(s,i)
                self.dfs(curr,i,l-1,r)
                
    def removeChar(self,s,i):
        head = s[:i]
        tail = s[i+1:]
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
