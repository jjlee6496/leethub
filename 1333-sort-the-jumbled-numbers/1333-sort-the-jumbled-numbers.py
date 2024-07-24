class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        order = []
        for num in nums:
            temp = ''
            for d in str(num):
                temp += str(mapping[int(d)])
            order.append((num, int(temp)))
        return [i[0] for i in sorted(order, key = lambda (x, y): y)]