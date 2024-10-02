class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        temp = sorted(set(arr))
        dic = {num:i for i, num in enumerate(temp, 1)}
        return [dic[num] for num in arr]

