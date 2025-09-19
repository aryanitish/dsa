# Solved on first attempt/approach
# Solution is time efficient but not space as I use a supporting list
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        A = [[1]]
        
        for i in range(1, numRows):
            B = [1]
            for j in range(i-1):
                B.append(A[i-1][j]+A[i-1][j+1])
            B.append(1)
            A.append(B)
        return A

