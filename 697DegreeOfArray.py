class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left,right,count = {},{},{}
        degree, res = 0,len(nums)
        for i,n in enumerate(nums):
            if n not in left:
                left[n] = i
            right[n] = i
            count[n] = count.get(n,0)+1
        degree = max(count.values())
        for i in count:
            if count[i] == degree:
                res = min(res,right[i]-left[i]+1)
        return res
