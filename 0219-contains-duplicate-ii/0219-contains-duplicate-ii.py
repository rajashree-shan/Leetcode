class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs={}

        for i,num in enumerate(nums):
            if num in hs:
                if i-hs[num]<=k:
                    return True

            hs[num]=i
        return False