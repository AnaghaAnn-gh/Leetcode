class Solution:
    def reverseWords(self, s: str) -> str:
        x=[]
        res = ""
        x=list(s.split())
        for i in range(len(x)-1 , -1, -1):
            res = res +  x[i] + " "
        res = res.strip(" ")
        return res
        

            
        
        