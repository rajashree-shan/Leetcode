class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]

            # move while consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            # close range
            if start != nums[i]:
                res.append(f"{start}->{nums[i]}")
            else:
                res.append(str(start))

            i += 1

        return res