class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone={
            "2":"abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res=[]
        def backtrack(index,current):

            if index==len(digits):
                res.append(current)
                return
            
            digit=digits[index]

            for letter in phone[digit]:
                backtrack(index+1,current+letter)

        backtrack(0,"")

        return res