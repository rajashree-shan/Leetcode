class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        result = []

        # Step 1: Add characters based on order
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]

        # Step 2: Add leftover characters
        for ch, freq in count.items():
            result.append(ch * freq)

        return "".join(result)
