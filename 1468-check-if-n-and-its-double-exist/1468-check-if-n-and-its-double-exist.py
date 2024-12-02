class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        s = set()
        for num in arr:
            if (2*num in s) or (num % 2 == 0 and num // 2 in s):
                return True
            s.add(num)
        return False
