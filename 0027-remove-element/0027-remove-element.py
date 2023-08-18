class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for j in range(len(nums)):
            for i in nums:
                if i==val:
                    nums.remove(val)
            

