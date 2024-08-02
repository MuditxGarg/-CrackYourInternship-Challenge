#Problem Statement
"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

#Solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix:
            return result

        row_start = 0
        row_end = len(matrix) - 1
        col_start = 0
        col_end = len(matrix[0]) - 1

        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1

            # Traverse down
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if row_start <= row_end:
                # Traverse left
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1

            if col_start <= col_end:
                # Traverse up
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1

        return result