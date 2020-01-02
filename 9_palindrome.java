class Solution {
    public boolean isPalindrome(int x) {
        int y=x;
        int result=0;
        if(x<0){
            return false;
        }else{
            while(y>0){
               result=10*result+(y%10);
               y=y/10;
            }
        
            if(result == x){
                return true;
            }else{
                return false;
            }
        }
        
    }
}