class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #linked list pbm
        #intersection point of slow and fast is returned
        #which will have an equal distance from the start of cycle and 0th index
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        #Floyd's cycle detection
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2 :
                return slow