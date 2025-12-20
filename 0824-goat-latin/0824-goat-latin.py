class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        result = []
        words = sentence.split()

        for i, j in enumerate(words, 1):
            if j[0] in vowels:
                goat = j + "ma"
            else:
                goat = j[1:] + j[0] + "ma"

            goat += "a" * i
            result.append(goat)

        return " ".join(result)





