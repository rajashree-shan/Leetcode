class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children=defaultdict(list)

        for emp,mgr in enumerate(manager):
            if mgr!=-1:
                children[mgr].append(emp)

        def dfs(employee):
            if not children[employee]:
                return 0
            max_time=0

            for child in children[employee]:
                max_time=max(max_time,dfs(child))
            return informTime[employee] + max_time
        return dfs(headID)

            
