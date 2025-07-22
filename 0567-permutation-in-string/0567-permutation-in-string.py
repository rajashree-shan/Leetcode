from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        s1_l=len(s1)
        s2_l=len(s2)
        if s1_l > s2_l:
            return False
        window_count = Counter(s2[:s1_l])
        if window_count == s1_count:
            return True 
                # Slide the window across s2
        for i in range(s1_l, s2_l):
            # Remove the leftmost character from the window
            left_char = s2[i - s1_l]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Add the new character to the window
            right_char = s2[i]
            window_count[right_char] += 1
            
            # Check if the current window matches s1_count
            if window_count == s1_count:
                return True
        return False