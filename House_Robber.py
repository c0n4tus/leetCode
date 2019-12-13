class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        df=[0]*len(nums)
        
        df[0]=nums[0]
        df[1]=max(nums[0],nums[1])

        for i in range(2,len(nums)):
            df[i]=max(nums[i]+df[i-2],df[i-1])
            
        return df[-1]
            