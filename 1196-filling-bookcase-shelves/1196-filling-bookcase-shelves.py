class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        mem = {}
        def dfs(i):
            if i == len(books):
                return 0
            if i in mem:
                return mem[i]
            cur_width = shelfWidth
            max_height = 0
            res = float('inf')
            for j in range(i, len(books)):
                width, height = books[j]

                if cur_width < width:
                    break
                
                cur_width -= width
                max_height = max(max_height, height)
                res = min(
                    res,
                    dfs(j + 1) + max_height
                )
            mem[i] = res
            return mem[i]
        return dfs(0)