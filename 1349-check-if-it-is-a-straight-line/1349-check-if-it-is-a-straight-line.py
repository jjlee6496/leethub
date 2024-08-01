class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def matrix_rank(matrix):
            def swap_row(mat, i, j):
                mat[i], mat[j] = mat[j], mat[i]

            def scale_row(mat, i, scale):
                mat[i] = [elem * scale for elem in mat[i]]

            def add_scaled_row(mat, i, j, scale):
                mat[i] = [elem_i + scale * elem_j for elem_i, elem_j in zip(mat[i], mat[j])]

            rows, cols = len(matrix), len(matrix[0])
            rank = 0
            for col in range(cols):
                if rank == rows:
                    break
                pivot_row = rank
                while pivot_row < rows and abs(matrix[pivot_row][col]) < 1e-10:
                    pivot_row += 1
                if pivot_row == rows:
                    continue
                swap_row(matrix, rank, pivot_row)
                scale_row(matrix, rank, 1.0 / matrix[rank][col])
                for i in range(rows):
                    if i != rank:
                        add_scaled_row(matrix, i, rank, -matrix[i][col])
                rank += 1
            return rank

        def are_collinear(*points):
            if len(points) < 3:
                return True  # 2개 이하의 점은 항상 한 직선 위에 있습니다.
            
            # 행렬 구성
            matrix = [[1, p[0], p[1]] for p in points]
            
            # 랭크 계산
            rank = matrix_rank(matrix)
            
            # 랭크가 2 이하이면 점들은 공선적입니다.
            return rank <= 2
        return are_collinear(*coordinates)