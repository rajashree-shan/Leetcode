class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_val=0
        max_val=0
        for i in nums:
            if i==1:
                curr_val+=1
                max_val=max(curr_val,max_val)
            else:
                curr_val=0
        return max_val