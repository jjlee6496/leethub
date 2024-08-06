class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """

        costs = [0] * 26
        cnt = Counter(word)
        for i, k in enumerate(sorted(cnt, key = lambda x: -cnt[x])):
            costs[ord(k) - ord('a')] += ((i // 8 + 1) * cnt[k])
        return sum(costs)