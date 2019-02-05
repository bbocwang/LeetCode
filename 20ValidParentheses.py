class Solution:
    def isValid(self, s: 'str') -> 'bool':
        p = []
        for i in s:
            if i == '(':
                p.append(')')
            elif i == '[':
                p.append(']')
            elif i == '{':
                p.append('}')
            elif i in [')',']','}']:
                if not p:
                    return False
                elif p and p[-1]==i:
                    p.pop()
                else:
                    return False
        if not p:
            return True
        else:
            return False       
