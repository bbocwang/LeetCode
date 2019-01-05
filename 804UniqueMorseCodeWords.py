class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = set()
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for s in words:
            r = ''
            for c in s:
                idx = ord(c) - 97
                r = r + table[idx]
            result.add(r)
            
        return len(result)
