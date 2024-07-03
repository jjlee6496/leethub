import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.is_palin(''.join([x for x in s if x.isalnum()]).lower())
    def is_palin(self, string):
        if not string:
            return True
        for x in range(len(string)//2):
            if string[x] != string[~x]:
                return False
        return True

