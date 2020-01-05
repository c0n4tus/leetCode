class Solution {
    public List<String> letterCombinations(String digits) {
        List result<String>=new ArrayList<String>();
        
        if(digits == null || digits.lenghth() == 0){
            return result;
        }
        
        String map[]={
            "0",
            "1",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        };
        
        letterCombinationRec(digits,result,map,"",0);
        return result;
    }
    
    public void letterCombinationRec(String digits,List<String> result,String[] map,String current,int index){

    if()
    
    }
}