class ProductOfNumbers(object):

    def __init__(self):
        self.mem = [1]
        self.n = 1 # pointer of present pos
        self.last_zero_ind = -1

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.last_zero_ind = self.n
        
        if self.mem[-1] == 0:
            self.mem.append(num)
        else:
            self.mem.append(self.mem[-1] * num)
        
        self.n += 1
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if self.last_zero_ind >= self.n - k:
            return 0
        if self.mem[self.n - k - 1] == 0: # to prevent zero division
            return self.mem[-1]
        else:
            return self.mem[-1] / self.mem[self.n - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)