class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        submission=[]
        cur=[]
        obj = Solution()
        return obj.combinationFinder(candidates, target, 0, cur, submission)
    

    def combinationFinder(self, candidates: List[int], target: int, index: int, cur: List[int], submission: List[List[int]]) -> List[List[int]]:
        if target < 0:
            return cur
        elif target == 0:
            submission.append(cur[:])
            return submission
        if index < len(candidates):
            value = candidates[index]
            cur.append(value)
            self.combinationFinder(candidates, target-value, index, cur, submission)
            cur.pop()
            self.combinationFinder(candidates, target, index+1, cur, submission)
        return submission
        