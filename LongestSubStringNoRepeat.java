
class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> dic=new HashSet();
        int a_pointer=0;
        int b_pointer=0;
        int max=0;
        if(s.length()==0){
            return 0;
        }
        
        while(b_pointer < s.length()){
            if(!dic.contains(s.charAt(b_pointer))){
                dic.add(s.charAt(b_pointer));
                b_pointer++;
                max=Math.max(max,dic.size());
            }else{
                dic.remove(s.charAt(a_pointer));
                a_pointer++;
            }
        }
        return max;
    }
}
  