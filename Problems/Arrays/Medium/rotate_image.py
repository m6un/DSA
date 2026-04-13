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