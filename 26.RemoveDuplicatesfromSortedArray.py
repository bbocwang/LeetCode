class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(set(nums))
        for i,k in enumerate(s):
            nums[i]=k
        return len(s)
