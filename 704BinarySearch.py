class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0,len(nums)-1
        if end == 0:
            if nums[0]==target: return 0
            else: return -1
        def bs(start,end,nums,target):
            if(start > end ): return -1
            mid = (start+end)//2
            if(nums[mid]==target): return mid
            elif(nums[mid]>target):
                return bs(start,mid-1,nums,target)
            elif(nums[mid]<target):
                return bs(mid+1,end,nums,target)
        return bs(start,end,nums,target)
