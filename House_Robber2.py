class Solution:
    
     def robRange(self, nums: List[int],start,end) -> int:       
        df=[0]*len(nums)
        df[start]=nums[start]
        df[start+1]=max(nums[start],nums[start+1])
        for i in range(start,end):
            df[i] = max(nums[i]+df[i-2],df[i-1])           
        return df[end-1]
                       
    
     def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
            return max(nums[0],nums[1], nums[2])
        else:
            return max(self.robRange(nums,0,len(nums)-1), 
                       self.robRange(nums,1,len(nums)))