from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)

        res=[]
        for num,freq in count.most_common():
            res.append(num*freq)
        return "".join(res)