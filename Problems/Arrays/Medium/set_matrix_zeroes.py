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