class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2 : return 0
        table=[True]*n
        table[0]=False
        table[1]=False
        for i in range(2,int(n**0.5)+1):
            if table[i]:
                for j in range(i**2,n,i):
                    table[j]=False
        return sum(table)
