class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest,second_largest=0,0
        for n in nums:
            if n>largest:
                second_largest=largest
                largest=n
            elif n>second_largest:
                second_largest=n

        return (largest-1)*(second_largest-1)