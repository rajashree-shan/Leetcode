class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1} 
        total = 0
        for i, num in enumerate(nums):
            total += num
            remainder = total % k

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        return False