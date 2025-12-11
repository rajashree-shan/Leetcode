class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n=len(matrix)
# 1) Push first element of each row
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

# 2) Pop k-1 times
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

# 3) k-th smallest = next top
        return heapq.heappop(min_heap)[0]