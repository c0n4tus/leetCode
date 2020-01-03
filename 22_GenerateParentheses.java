class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> comb=new ArrayList();
        backTrack("",n,comb,0,0);
        return comb;
    }
    
    public void backTrack(String s, int max,List<String> comb,int left,int right){
        
        if(s.length()== max*2) {
            comb.add(s);
            return;
        }else{
            if(left < max){
                backTrack(s+"(",max,comb,left+1,right);
            }
            if(right < left){
                backTrack(s+")",max,comb,left,right+1);
            }
            
            
        }
        
        
        
    }
}