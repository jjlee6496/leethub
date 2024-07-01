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
            if num % 2:
                cnt += 1
                if cnt == 3:
                    return True
            else:
                cnt = 0
        return False
    