class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int dp[] = new int[n];
        for(int i=0;i<n;i++){
            dp[i] = 1;
            for(int j=0;j<i;j++){
                if(dp[j] >= dp[i] && nums[j] < nums[i]){
                    dp[i] = dp[j] + 1;
                }
            }
        }
        int max = 0;
        for(int i=0;i<n;i++){
            if(dp[i] > max)
                max = dp[i];
        }
        return max;
    }
}
