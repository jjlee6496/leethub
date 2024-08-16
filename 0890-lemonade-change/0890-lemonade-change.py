class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        coins = [0]*2
        for b in bills:
            if b == 5:
                coins[0] += 1
            elif b == 10:
                if not coins[0]:
                    return False
                coins[0] -= 1
                coins[1] += 1
            else:
                if coins[1] and coins[0]:
                    coins[1] -= 1
                    coins[0] -= 1
                elif not coins[1]:
                    if coins[0] < 3:
                        return False
                    coins[0] -= 3
                else:
                    return False
        return True

