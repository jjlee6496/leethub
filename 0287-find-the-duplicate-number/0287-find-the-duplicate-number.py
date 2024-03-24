class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        turtoise = hare = nums[0]
        while True:
            turtoise = nums[turtoise]
            hare = nums[nums[hare]]
            if turtoise == hare:
                break
        
        ptr1 = nums[0]
        ptr2 = turtoise

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
