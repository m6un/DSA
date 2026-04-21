"""
Problem: Pascal's triangle
Difficulty: E
Link: https://leetcode.com/problems/pascals-triangle/description/
"""
class Solution:
    def solution_optimized(self, numRows: int) -> List[List[int]]:
        """
        Intuition: Damnnn, I just did a DP question w/o any help and got it right the first time lessgo. The intuition here is: 
        1. You need to understand that the array that comes below an array will have values that are the sum of values of the array just above it, but with one caveat -- the first and last elements of our array will be 1. And to calculate the middle one you do the sum of the above array element at the same place + element one index before. 
        2. The first element will be [1], this is known but can't be calculated so it's an edge case you need to handle.

        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        Reasoning : SC is so because we're returning back an array of the size 1+2+3+..+n = n(n+1)/2 which would be O(n^2). Now this is output data structure space. There'll be an auxiliary space of O(2n), which would cancel out when added with O(n^2). hence the SC is O(N^2)
        """
        result = []
        for i in range(1, numRows+1):
            #what do we need here ? 
            if len(result) == 0:
                result.append([1]) 
                continue
            prev = result[-1]
            arr = [1] * i
            for j in range(1,i-1):
                arr[j] = prev[j-1] + prev[j]
            result.append(arr)
        return result1