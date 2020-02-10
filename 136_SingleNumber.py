class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for a in range(0,len(nums)):
            if not dic:
                dic[nums[a]]=nums[a];
            elif dic.get(nums[a]):
                dic.pop(nums[a])
            elif nums[a] == 0 and dic.get(nums[a]) == 0:
                dic.pop(nums[a])
            else:
                dic[nums[a]]=nums[a];
                
        for a in dic:
            return dic.get(a)
        
                    