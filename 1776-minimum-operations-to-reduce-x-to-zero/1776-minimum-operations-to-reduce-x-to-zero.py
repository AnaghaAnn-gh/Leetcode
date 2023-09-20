class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        current_sum = 0
        max_window = -1 
        #sliding window approach is used here to minimize the time complexity to O(n)

        l = 0
        for r in range(len(nums)):
            current_sum += nums[r]

            while l <= r and current_sum > target:
                current_sum -= nums[l]
                l += 1
            if current_sum == target:
                max_window = max(max_window, r - l + 1)

        if max_window == -1:
            return -1
        else:
            return len(nums) - max_window

