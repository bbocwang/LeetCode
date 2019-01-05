class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for s in emails:
            idx = s.find('@')
            idx1 = s.find('+')
            if idx1 != -1:
                s = s[:idx1]+s[idx:]
            idx2 = s.find('@')
            s1 = s[:idx2].replace('.',"")
            result.add(s1+s[idx2:])
        return len(result)
