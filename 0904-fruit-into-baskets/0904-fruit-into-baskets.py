class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        maxi = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi