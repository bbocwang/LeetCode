class Solution {
    public int addDigits(int num) {
        String number = Integer.toString(num);
        while(number.length() >1){
            number = add(number);
        }
        return Integer.parseInt(number);
    }
    
    public String add(String number){
        int len = number.length(), i = 0, res = 0;
        while(i <= len - 1){
            res += number.charAt(i++) - '0';
        }
        return Integer.toString(res);
    }
}




class Solution {
    public int addDigits(int num) {
        return num == 0 ? 0 : (num % 9 == 0 ? 9 : (num % 9));
    }
}
