class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Variable to track the maximum length

        for right in range(len(s)):  # Right pointer expands the window
            # If a duplicate is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set and update max_length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length