class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            largest = i
            l, r = 2*i+1, 2*i+2
            if l < n and nums[l] > nums[largest]:
                largest = l
            if r < n and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        n = len(nums)
        for i in range(n//2-1, -1, -1):
            heapify(n, i)
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(i, 0)
        return nums