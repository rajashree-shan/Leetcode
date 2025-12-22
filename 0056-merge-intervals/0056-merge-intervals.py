class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            Last_end=output[-1][1]
            if start<=Last_end:
                output[-1][1]=max(Last_end,end)
            else:
                output.append([start,end])
        return output
