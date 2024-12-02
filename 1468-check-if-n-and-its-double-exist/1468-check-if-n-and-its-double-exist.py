class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        l = 0
        for r in range(len(arr)):
            if arr[l] * 2 > arr[r]:
                continue
            temp = l
            while l < r:
                if arr[l] * 2 == arr[r] or arr[r] * 2 == arr[l]:
                    return True
                l += 1
            l = temp
        return False
