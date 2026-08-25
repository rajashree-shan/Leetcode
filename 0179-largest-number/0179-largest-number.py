class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        arr = []

        # Convert every number into a string
        for num in nums:
            arr.append(str(num))

        # Get length AFTER filling arr
        n = len(arr)

        # Bubble sort
        for i in range(n):

            for j in range(n - 1 - i):

                # Decide which order creates a bigger number
                if arr[j] + arr[j + 1] < arr[j + 1] + arr[j]:

                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        result = ""

        # arr contains strings, so use arr
        for num in arr:
            result += num

        # Handle [0, 0] -> "0", not "00"
        if result[0] == "0":
            return "0"

        return result