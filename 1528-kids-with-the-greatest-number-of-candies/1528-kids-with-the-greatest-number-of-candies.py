class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candy = max(candies)
        
        for i in range(len(candies)):
            
            if (candies[i] + extraCandies) < max_candy:
                res.append(False)
            else:
                res.append(True)
        return res