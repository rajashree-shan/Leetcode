class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs={}
        for i,j in enumerate(nums):
            diff=target-nums[i]
            if diff in hs:
                return hs[diff],i
            hs[j]=i