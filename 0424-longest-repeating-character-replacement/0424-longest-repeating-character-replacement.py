class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # Start of the sliding window
        max_count = 0  # To track the count of the most frequent character in the window
        char_count = {}  # Dictionary to store the frequency of characters
        max_length = 0  # To store the maximum length of the substring

        for right in range(len(s)):
            # Update the frequency of the current character
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Track the most frequent character count in the current window
            max_count = max(max_count, char_count[s[right]])

            # If the number of replacements needed exceeds k, shrink the window
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum length of the valid substring
            max_length = max(max_length, right - left + 1)

        return max_length