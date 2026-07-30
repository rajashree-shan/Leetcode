class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0

        for i in range(len(word)):
            answer += (i // 8) + 1

        return answer