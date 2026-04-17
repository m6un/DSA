"""
Problem: Spiral matrix
Difficulty: Medium
Link: https://leetcode.com/problems/spiral-matrix/
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Intuition: Okay so the intuition here's basically to keep the gates , top left bottom and right and then progressively keep reducing them and after every step checking if the gates have been breached. One key learning here for me is while loop + manually making changes to the pointer, then better to use a for loop for that. 
        The intuition is to follow a simulation : We go boundary by boundary and move inwards. That's the essential operation. First row, last column, last row, first column and then we move inwards by 1 and repeat

        Time Complexity: O(M x N)
        Space Complexity: O(1)
        Reasoning : TC obvious. For SC , we're returning a result array of length M*N, but in many contexts, we don't count the result array towards counting the SC.
        """
    
        i = 0 
        j = 0
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        result = []
        while True:
            
            for j in range(left, right+1):
                result.append(matrix[i][j])
            top += 1
            if left > right or top > bottom :
                return result

            for i in range(top, bottom+1):
                result.append(matrix[i][j])
            right -= 1
            if left > right or top > bottom :
                return result

            for j in range(right, left-1, -1):
                result.append(matrix[i][j])
            bottom -= 1
            if left > right or top > bottom :
                return result

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][j])
            left += 1
            if left > right or top > bottom :
                return result