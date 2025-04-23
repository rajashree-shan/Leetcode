class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.strip().split()
        return ' '.join(reversed(w))
