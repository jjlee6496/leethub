class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_q = deque() # monotonic increasing
        max_q = deque() # monotonic decreasing
        left = 0
        res = 0

        for right in range(len(nums)):
            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
        
            min_q.append(nums[right])
            max_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                if min_q[0] == nums[left]:
                    min_q.popleft()
                if max_q[0] == nums[left]:
                    max_q.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res