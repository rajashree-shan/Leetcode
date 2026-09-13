class Solution:
    def combinationSum(self, candidates, target):

        candidates.sort()

        result = []
        path = []

        def backtrack(i, remaining):

            if remaining == 0:
                result.append(path[:])
                return

            if remaining < candidates[i]:
                return

            for j in range(i, len(candidates)):

                path.append(candidates[j])

                backtrack(j,remaining - candidates[j])

                path.pop()

        backtrack(0, target)

        return result