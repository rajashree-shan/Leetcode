class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count=Counter(ransomNote)
        m_count=Counter(magazine)
        for ch in r_count:
            if m_count[ch]<r_count[ch]:
                return False
        return True