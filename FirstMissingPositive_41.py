class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=1
        dic={}
        dic[1]=1
        for i in range(0,len(nums)):
            if nums[i] < s and nums[i] > 0 and not dic.get(nums[i]):
                dic[nums[i]]=nums[i]
                s=nums[i]
            elif nums[i] == s :
                if dic.get(s+1):
                    j=s+1
                    while dic.get(j) != None:
                        j=j+1
                    s=j
                    dic[nums[i]]=nums[i]
                else:
                    s=s+1
                    dic[nums[i]]=nums[i]
            else:
                dic[nums[i]]=nums[i]
               
        return s