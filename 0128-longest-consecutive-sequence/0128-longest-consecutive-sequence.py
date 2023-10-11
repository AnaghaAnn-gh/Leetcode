class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 #length of the longest sequence so far

        for n in nums:
            #checks if the number before n exists, 
            #if it doesnot then n is the start of a sequence
            length = 0 #length of a sequence
            if n-1 not in numSet: 
                while n+length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
        
            