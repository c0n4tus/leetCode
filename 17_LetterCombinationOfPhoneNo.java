class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result=new ArrayList<String>();
        
        if(digits == null || digits.length() == 0){
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

    if(index == digits.length()){
        result.add(current);
        return;
    }
    
        String letter = map[Character.getNumericValue(digits.charAt(index))];
        for(int i=0;i<letter.length();i++){
            letterCombinationRec(digits,result,map,current+letter.charAt(i),index+1);
        }
        
    }
}