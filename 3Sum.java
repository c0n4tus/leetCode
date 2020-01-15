import java.util.Arrays; 
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<Integer> subList=new ArrayList<>();
        List<List<Integer>> result=new ArrayList<>();
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++){
            if(i == 0 || (i>0 && nums[i] != nums[i-1])){
            int first=i+1;
            int last =nums.length-1;
            int sum=0-nums[i];
            while(first < last){
                
                if((nums[first]+nums[last]) == sum){
                    subList=new ArrayList<>();
                    subList.add(nums[i]);
                    subList.add(nums[first]);
                    subList.add(nums[last]);
                    result.add(subList);
                    while(first < last && nums[first] == nums[first+1]) first++;
                    while(first < last && nums[last] == nums[last-1]) last--;
                    first++;
                    last--;
                }else if((nums[first]+nums[last]) < sum){
                    first+=1;
                }else{
                    last-=1;
                }
            }
            }
            
        }
       return result; 
    }
}