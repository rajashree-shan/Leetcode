class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        n=len(nums)
        curr_end=0
        farthest=0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == curr_end:               # finished current "level"
                jumps += 1
                curr_end = farthest         # move to next level boundary

        return jumps
