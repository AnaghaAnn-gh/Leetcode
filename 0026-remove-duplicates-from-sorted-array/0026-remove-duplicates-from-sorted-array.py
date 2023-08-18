class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]>temp:
                temp=nums[i]
                nums[count]=temp
                count+=1
        return count
