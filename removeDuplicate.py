class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic={}
        length=len(nums)-1
        i=0
        while i <= length:
            if nums[i] == 0 and not dic.get(0):
                dic[0]=1
                i=i+1
            if not dic.get(nums[i]):
                dic[nums[i]]=nums[i]
                i=i+1
            else:
                nums.pop(i)
                length=length-1