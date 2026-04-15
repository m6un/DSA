"""
Problem: Spiral matrix
Difficulty: Medium
Link: https://leetcode.com/problems/spiral-matrix/
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Intuition: 

        Time Complexity: O()
        Space Complexity: O()
        Reasoning : 
        """
        """
        Hmm, from the hints, they're saying that for some problems we need to write
        algorithm for the simulation. And the simulation here, 
        We go boundary by boundary and move inwards. That's the essential operation. 
        First row, last column, last row, first column and then we move inwards by 1 and
        repeat -- This is the simulation that we need interesting. Even I got here, but my 
        question was more around how we'll figure out okay now I should stop here and move
        inwards hmmmm. But now that I've heard it explicitly, I've got the idea it seems. 
        """
        '''
        one question is how do you know when to stop as in, we should know that we can't
        go into a place where we've passed once. I mean if we keep updating the i below, and 
        if the next step of the new cycle by any chance ( this goes after the intial step)
        tries to get into the line of the i then we stop. I know this doesn't make sense rn,
        but lemme code this out ( both the end columns )
        '''
        #let i be where we start one cycle before we go inward. 
        i = 0 
        j = 0
        left_most_column_index = 0
        right_most_column_index = len(matrix[0]) - 1
        top_row_index = 0
        bottom_row_index = len(matrix) - 1
        cycle_starting_column_index = 0
        result = []
        while j <= right_most_column_index:
            result.append(matrix[i][j])
            j+= 1

        i+= 1
        j-= 1
        while i <= bottom_row_index:
            result.append(matrix[i][j])
            i+= 1
        
        j -= 1 
        i-= 1
        while j >= left_most_column_index:
            result.append(matrix[i][j])
            j -= 1
        
        i-= 1 
        j+= 1
        while i >= cycle_starting_column_index:
            print(f"{i},{j}")
            result.append(matrix[i][j])
            i -= 1
        i += 1
        return result