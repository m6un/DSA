"""
Problem: Rotate image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/description/
"""
class Solution:
    def unconventional_optimal_solution(self, matrix: List[List[int]]) -> None:
        """
        Intuition: I have absolutely no idea how I came into this solution lmao. But yeah let's give it a try. So the idea is the first column and the last row needs to swap places. Now the second column and the second last row , except the members of the first col and last row need to swap and we'll keep swapping like think until there's only one element left at the top right. basically until we reach the top right'th element.

        Time Complexity: O(N^2)
        Space Complexity: O(1)
        Reasoning : obv
        """
        n = len(matrix)
        for k in range(n):
            # i = matrix[k][0]
            # j = matrix[n-1-k][n-1]
            i = 0
            j = n-1
            while f"{i}{k}" != f"{n-1-k}{j}":
                print(f"{i} {k}", f"{n-1-k} {j}")
                matrix[i][k] , matrix[n-1-k][j] = matrix[n-1-k][j], matrix[i][k]
                i += 1
                j -= 1
        
        i = 0
        j = n-1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i+= 1
            j -= 1
    
        def conventional_optimal_solution(self, matrix: List[List[int]]) -> None:
            """
            Intuition: Here the intuition is to do the transpose of the matrix - see below how it's done I believe this would be the common step to do in upcoming matrix questions as well. We'll just split the matrix into upper and lower triangles divided by the diagonal and then swap the corresponding values. and then just reverse each array

            Time Complexity: O(N^2)
            Space Complexity: O(1)
            Reasoning : obv
            """
            n = len(matrix)
            
            # 1. Transpose the matrix
            # We only iterate over the upper triangle to avoid swapping back j starting from i+1 allows that
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # 2. Reflect (Reverse each row)
            for i in range(n):
                matrix[i].reverse()