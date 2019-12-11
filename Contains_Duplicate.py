class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={} 
        for i in range(0,len(nums)):
            if dic:
                if dic.get(nums[i]) == None:
                    dic[nums[i]]=nums[i]
                elif dic.get(nums[i]) == 0 and nums[i] == 0:
                    return True
                elif dic.get(nums[i]):
                    return True
            else:
                dic[nums[i]]=nums[i]
        return False