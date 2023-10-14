class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            Prev_end = result[-1][1]
            if start <= Prev_end:
                result[-1][1] = max(Prev_end, end)
            else:
                result.append([start, end])
        return result
