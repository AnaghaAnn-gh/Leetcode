class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        result=0
        for i in nums:
            if count==0:
                result=i
            if result==i:
                count+=1
            else:
                count-=1
        return result
            
