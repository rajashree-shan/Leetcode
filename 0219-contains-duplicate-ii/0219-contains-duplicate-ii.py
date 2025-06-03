class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs=set()
        j=0
        for i in range(len(nums)):
            if i-j>k:
                hs.remove(nums[j])
                j=j+1
            if nums[i] in hs:
                return True
            hs.add(nums[i])
        return False
        