class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        tmp = []

        for i,j in enumerate(mat):
            x = (sum(j), i)
            tmp.append(x)
        tmp.sort()

        return [i[1] for i in tmp[:k]]
        


    