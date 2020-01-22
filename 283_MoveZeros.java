class Solution {
    public void moveZeroes(int[] nums) {
        
        for(int i=0;i<nums.length;i++){
            int j=i+1;
            if(nums[i] == 0){
                while(j < nums.length){
                if(nums[j] != 0){
                    int temp=nums[j];
                    nums[j]=nums[i];
                    nums[i]=temp;
                    break;
                }else if(nums[j] == 0){
                    j++;
                }
            }
        }
    }
  }
}