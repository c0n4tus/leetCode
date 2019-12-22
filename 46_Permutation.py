class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        start=0
        result=[]
        return self.permuteHelper(start,nums,result)
        
        
    def permuteHelper(self,start:int,nums:List[int],result:List[List[int]])-> List[List[int]]:
        if start >= len(nums):
            result.append(nums[:])
        else:
            for j in range(start,len(nums)):
                self.swap(j,start,nums)
                self.permuteHelper(start+1,nums,result)
                self.swap(j,start,nums)
        return result
                
                
    def swap(self,j:int,start:int,nums:List[int]):
        temp=nums[j]
        nums[j]=nums[start]
        nums[start]=temp
    