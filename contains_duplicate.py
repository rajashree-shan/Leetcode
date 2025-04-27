class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs=set()

        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False
