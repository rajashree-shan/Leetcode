class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l_mult=1
        r_mult=1
        l_array=[0] * n
        r_array=[0] * n
        for i in range(n):
            j= -i -1
            l_array[i]=l_mult
            r_array[j]=r_mult
            l_mult*=nums[i]
            r_mult*=nums[j]
        return [l*r for l,r in zip(l_array,r_array)]


