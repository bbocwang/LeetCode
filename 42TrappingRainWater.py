#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (41.38%)
# Total Accepted:    246.4K
# Total Submissions: 595.6K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#
class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        dp = [[0 for i in range(2)]for i in range(len(height))]
        res=0
        for i in range(len(height)):
            maxl,maxr,sum = 0,0,0
            if i != 0:
                maxl = max(dp[i-1][0],height[i-1])
                dp[i][0] = maxl
        for i in reversed(range(len(height))):
            if i!= len(height)-1:
                maxr = max(dp[i+1][1],height[i+1])
                dp[i][1]=maxr
            sum = min(dp[i]) - height[i]
            if sum > 0 :
                res += sum
        return res
