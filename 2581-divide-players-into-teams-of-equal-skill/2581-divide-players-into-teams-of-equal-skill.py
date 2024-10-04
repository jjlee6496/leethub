class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        l, r = 0, len(skill) - 1
        res = 0
        k = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] == k:
                res += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1
        return res