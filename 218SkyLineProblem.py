class Solution:
    import heapq
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        elif len(buildings)==1:
            return [[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
        
        mid = len(buildings)//2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        i,j = 0,0
        h1,h2 = 0,0
        res=[]
        while i<len(left) and j<len(right):
            if left[i][0]<right[j][0]:
                h1 = left[i][1]
                new = [left[i][0],max(h1,h2)]
                i+=1
                if not res or res[-1][1]!=new[1]:
                    res.append(new)
            elif left[i][0]>right[j][0]:
                h2 = right[j][1]
                new = [right[j][0],max(h1,h2)]
                j+=1
                if not res or res[-1][1]!=new[1]:
                    res.append(new)
            else:
                h1 = left[i][1]
                h2 = right[j][1]
                new = [left[i][0],max(h1,h2)]
                i+=1
                j+=1
                if not res or res[-1][1]!=new[1]:
                    res.append(new)
            
        while i<len(left):
            h1 = left[i][1]
            new = [left[i][0],max(h1,h2)]
            i+=1
            if not res or res[-1][1]!=new[1]:
                    res.append(new)
        while j<len(right):
            h2 = right[j][1]
            new = [right[j][0],max(h1,h2)]
            j+=1
            if not res or res[-1][1]!=new[1]:
                res.append(new)
        return res
