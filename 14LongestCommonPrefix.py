class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        length = 1000
        for i in strs:
            if len(i)<length:
                length = len(i)
        if length == 0:
            return ''
        for i in range(length):
            check = True
            for j in strs:
                if j[i] != strs[0][i]:
                    check = False
                    return res
            if check:
                res += strs[0][i]
        return res
                
        
