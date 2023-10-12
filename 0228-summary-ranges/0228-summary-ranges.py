class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start_index = 0
        res = []

        for i in range(len(nums)):
        # Find last index for continuous series
            if i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                continue

            if start_index == i:
                res.append(str(nums[start_index]))
            else:
                res.append(str(nums[start_index]) + "->" + str(nums[i]))

            start_index = i + 1

        return res