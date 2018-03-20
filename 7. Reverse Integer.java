class Solution {
    public int reverse(int x) {
        if(x > Integer.MAX_VALUE || x < Integer.MIN_VALUE){
            return 0;
        }
        long result = 0;
         while(x != 0){
            result = result*10 + x%10;
            x = x/10;
             if(result > Integer.MAX_VALUE || result < Integer.MIN_VALUE){
            return 0;
        }
        }
        return (int)result;
    }
}
