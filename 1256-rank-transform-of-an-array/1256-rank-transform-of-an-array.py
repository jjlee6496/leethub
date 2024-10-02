class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dic = {}
        temp = sorted(arr)
        i = 1
        for num in temp:
            if num in dic:
                continue
            dic[num] = i
            i += 1
        return [dic[num] for num in arr]

