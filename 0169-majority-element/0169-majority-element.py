class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans=count=0
        for i in nums:
            if count==0:
                ans=i
            count+= (1 if i==ans else -1)
        return ans