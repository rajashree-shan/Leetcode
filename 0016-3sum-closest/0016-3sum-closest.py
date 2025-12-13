class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        best_sum = nums[0] + nums[1] + nums[2]

        for fixed in range(n - 2):
            left = fixed + 1
            right = n - 1

            while left < right:
                current_sum = nums[fixed] + nums[left] + nums[right]

                
                if abs(target - current_sum) < abs(target - best_sum):
                    best_sum = current_sum

                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum  

        return best_sum
