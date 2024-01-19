class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()      
        
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s > 0:
                    right -= 1

                elif s < 0:
                    left += 1

                else:
                    answer.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    left += 1
                    right -= 1
        
        return answer
