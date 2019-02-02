class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #find the pivot in O(lgn)
        def findMid(l,r,nums):
            mid=(l+r)//2
            if mid==0 or mid == len(nums)-1 or (nums[mid]>nums[mid-1]and nums[mid]>nums[mid+1]):
                return mid
            elif nums[mid]<nums[l]:
                return findMid(l,mid,nums)
            elif nums[mid]>nums[r]:
                return findMid(mid,r,nums)
        if not nums:return -1
        mid = findMid(0,len(nums)-1,nums)
        def bs(l,r,nums,target):
            if l>r:return -1
            mid1 = (l+r)//2
            if(nums[mid1]==target):return mid1
            elif nums[mid1]>target:
                return bs(l,mid1-1,nums,target)
            elif nums[mid1]<target:
                return bs(mid1+1,r,nums,target)
        l,r = 0,len(nums)-1
        if mid == None:
            return bs(l,r,nums,target)
        else:
            res1,res2 = bs(l,mid,nums,target),bs(mid+1,r,nums,target)
            return max(res1,res2)
