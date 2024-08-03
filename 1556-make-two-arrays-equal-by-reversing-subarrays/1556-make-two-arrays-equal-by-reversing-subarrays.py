class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        for a, t in zip(arr, target):
            dic1[a] = dic1.get(a, 0) + 1
            dic2[t] = dic2.get(t, 0) + 1

        return dic1 == dic2
