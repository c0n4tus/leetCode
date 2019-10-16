class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        pair=[]
        for i in range(0,len(nums)):
            s=target - nums[i]
            if not map1 or (map1.get(s) == None):
               map1[nums[i]] = target-nums[i]
            elif map1.get(s):
                pair=[nums.index(s), i]
                break
            elif map1.get(s) == 0:
                 pair=[nums.index(s), i]
                 break
        return pair
