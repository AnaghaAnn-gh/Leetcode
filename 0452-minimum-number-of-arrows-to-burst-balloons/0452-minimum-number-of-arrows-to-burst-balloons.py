class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        count = 1
        points.sort(key = lambda i : i[0])
        end = points[0][1]
        for i in range(len(points)):
            if end < points[i][0] :
                end = points[i][1]
                count += 1
            else:
                end = min(points[i][1], end)
        return count