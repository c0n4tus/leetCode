class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        for a in range(0,len(nums)):
            if not dic:
                dic[nums[a]]=1
            elif dic.get(nums[a]) is None:
                #dic.pop(list(dic.keys())[-1]);
                dic[nums[a]]=1
            else:
                dic[nums[a]]=dic.get(nums[a])+1
        max=0
        no=0
        for a in dic:
            if (dic.get(a) > max) and (dic.get(a) > len(nums)/2):
                max=dic.get(a)
                no=a
                
        return no
                
            
            
        