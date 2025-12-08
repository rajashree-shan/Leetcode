class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        # Step 1: move while chars match
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1

        # If we finished, it's already a palindrome
        if left >= right:
            return True

        # Now we found the FIRST mismatch at (left, right)
        # Option 1: skip s[left]
        i = left + 1
        j = right
        ok1 = True
        while i < j:
            if s[i] != s[j]:
                ok1 = False
                break
            i += 1
            j -= 1

        if ok1:
            return True

        # Option 2: skip s[right]
        i = left
        j = right - 1
        ok2 = True
        while i < j:
            if s[i] != s[j]:
                ok2 = False
                break
            i += 1
            j -= 1

        return ok2
