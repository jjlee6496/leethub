class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize:
            return False
        cnt = Counter(hand)
        while cnt:
            num = min(cnt.keys())
            for _ in range(groupSize):
                if not cnt[num]:
                    return False
                cnt[num] -= 1
                if not cnt[num]:
                    del cnt[num]
                num += 1 
        return True
