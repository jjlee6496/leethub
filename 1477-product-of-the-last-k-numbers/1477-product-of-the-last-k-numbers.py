class ProductOfNumbers(object):

    def __init__(self):
        self.mem = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.mem = [1]
        else:
            self.mem.append(self.mem[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.mem):
            return 0
        return self.mem[-1] / self.mem[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)