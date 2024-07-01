class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        cnt = 0
        for num in arr:
            if cnt == 3:
                return True
            if num % 2:
                cnt += 1
            else:
                cnt = 0
        return cnt == 3
    