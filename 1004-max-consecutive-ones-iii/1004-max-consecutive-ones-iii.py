class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            # Include nums[right] in the window
            if nums[right] == 0:
                zero_count += 1

            # If more than k zeros, shrink from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Now window [left, right] has at most k zeros
            current_window_length = right - left + 1
            if current_window_length > max_len:
                max_len = current_window_length

        return max_len
