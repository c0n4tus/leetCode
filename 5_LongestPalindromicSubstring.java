class Solution {
    private int lo, maxLen;
    public String longestPalindrome(String s) {
        int start=0;
        int end=0;
        for(int i=0;i<s.length();i++){
            startFromMiddle(i,i,s); //racecar
            startFromMiddle(i,i+1,s); //aaabbaaa
        }
       
        return s.substring(lo,maxLen+lo);
    }
    
    public void startFromMiddle(int start,int end,String s){
      
        while(start >=0 && end < s.length() &&  s.charAt(start) == s.charAt(end)){
            start-=1;
            end+=1;
        }
        if (maxLen < end-start-1) {
        lo=start+1;
        maxLen=end-start-1;
        }
        } 
    }

