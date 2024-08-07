class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        self.tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        self.ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        def threedigit(num):
            res = []
            for x in [2, 1, 0]:
                p = 10 ** x
                if num // p:
                    if x == 2:
                        res.append("{} hundred".format(self.ones[num // p]))
                    if x == 1:
                        if num // p == 1:
                            res.append("{}".format(self.teens[num % p]))
                            break
                        else:
                            res.append("{}".format(self.tens[num // p]))
                    if x == 0:
                        res.append("{}".format(self.ones[num // p]))
                num -= p * (num // p)
            return " ".join(res)
        capitalize = lambda s: " ".join(w[0].upper() + w[1:] for w in s.split())
        res = []
        for x in [9, 6, 3, 0]:
            p = 10 ** x
            if num // p:
                if x == 9:
                    res.append("{} billion".format(threedigit(num // p)))
                if x == 6:
                    res.append("{} million".format(threedigit(num // p)))
                if x == 3:
                    res.append("{} thousand".format(threedigit(num // p)))
                if x == 0:
                    res.append("{}".format(threedigit(num // p)))
            num -= p * (num // p)
        return capitalize(" ".join(res))