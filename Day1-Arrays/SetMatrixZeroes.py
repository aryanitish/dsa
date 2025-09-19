# First attempt. Fails test as tries to do in-place and counts the replaced 
# zeroes as inputs and makes the corresponding rows and columns zero
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for k in range(n):
                        matrix[i][k]=0
                    for k in range(m):
                        matrix[k][j]=0

# Second attempt. Solution works but probably brute force and bad timing
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        make_zero_row = set()
        make_zero_column = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    make_zero_row.add(i)
                    make_zero_column.add(j)

        for i in make_zero_row:
            for j in range(n):
                matrix[i][j]=0
        for i in range(m):
            for j in make_zero_column:
                matrix[i][j]=0
