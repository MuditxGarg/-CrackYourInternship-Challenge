#Problem Statement
'''
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's.

You must do it in place.
'''

#solution
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        rows = []
        cols = []

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        
        for i in rows:
            for j in range(c):
                matrix[i][j] = 0
        
        for j in cols:
            for i in range(r):
                matrix[i][j] = 0