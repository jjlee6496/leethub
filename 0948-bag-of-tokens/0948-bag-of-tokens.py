class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        res = score = 0
        l, r = 0, len(tokens) - 1
        tokens.sort()

        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                res = max(score, res)

            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break

        return res