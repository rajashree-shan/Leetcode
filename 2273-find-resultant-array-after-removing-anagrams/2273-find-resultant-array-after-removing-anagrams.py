class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer=[]
        for i in words:
            if not answer:
                answer.append(i)
            else:
                last_word=answer[-1]

                if sorted(i)!=sorted(last_word):
                    answer.append(i)
        return answer