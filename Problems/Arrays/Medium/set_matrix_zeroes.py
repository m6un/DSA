"""
Problem: Set Matrix zeroes
Difficulty: Medium
Link: https://leetcode.com/problems/set-matrix-zeroes/
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Intuition: Uhh, I was just trying to get this done bruteforce way. We did with with o(mn) TC and o(m+n) SC. The optimal solution here should have SC as O(1). I shouldn't use any extra data structures, but use the matrix itself. And the idea I got from Gemini, as a hint is to look at the first column and row to store these flags for the rest of the matrix. hmmm.

        Time Complexity: O(M x N)
        Space Complexity: O(N)
        Reasoning : TC - obvious. SC - because imagine if the matrix contains diagonal zeroes, we'll have to store one index for every column in the matrix - making it propotional to N
        """
        zero_index_array = []
        def zero_index(arr):
            set_whole_array_zero = False
            for i in range(len(arr)):
                if arr[i] == 0:
                    zero_index_array.append(i)
                    set_whole_array_zero = True
            if set_whole_array_zero == True:
                for i in range(len(arr)):
                    arr[i] = 0
                    
        #bruteforce
        for arr in matrix:
            zero_index(arr)
        
        if len(zero_index_array) != 0:
            for arr in matrix:
                for i in zero_index_array:
                    arr[i] = 0

    def setZeroesFollowup(self, matrix: List[List[int]]) -> None:
        """
        Intuition: Okay so the followup was to do this in O(1) space. The hint is to use the first row and first column as flags for which arrays in the matrix you need to zero out. I got it done, but the implementation here is a cleaned up one that i got from Gemini, I feel this one's the right mental model to follow as well. you modify the header row and first column, use that to fix the sub-matrix , which is the part of the matrix excluding the first row and first column, then go on to fix the first row and column, in case they had zeroes in the first place.

        Time Complexity: O(M x N)
        Space Complexity: O(1)
        Reasoning : TC - obv , SC - bc we're not using any extra data structures. 
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero = False
        
        # 1. Determine if the first row needs to be zeroed later
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # 2. Use the first row and first column as markers
        # We start from row 1 because row 0 is our "header"
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # 3. Fill zeros based on markers (excluding first row/column for now)
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 ## like this a lot. This is the way to do these problems I feel. 

        # 4. Handle the first column (if first element is 0, entire column is 0)
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        # 5. Finally, handle the first row using our boolean flag
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0