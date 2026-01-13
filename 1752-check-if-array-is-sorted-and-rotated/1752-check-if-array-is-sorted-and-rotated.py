class Solution:
    def check(self, nums: List[int]) -> bool:
        drops=0
        n=len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                drops+=1
        if nums[-1]>nums[0]:
            drops+=1
        return drops<=1