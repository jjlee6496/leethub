class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # 아무 책도 없음

        for i in range(1, n + 1):
            cur_width = shelfWidth
            max_height = 0
            for j in range(i - 1, -1, -1):
                width, height = books[j]
                if cur_width < width:
                    break
                cur_width -= width
                max_height = max(max_height, height)
                dp[i] = min(
                    dp[i],
                    dp[j] + max_height
                )
        return dp[n]