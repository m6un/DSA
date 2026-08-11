"""
Problem: Kth Missing positive number
Difficulty: Easy
Link: https://leetcode.com/problems/kth-missing-positive-number/description/
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Intuition: This is very logical. 
        - For an array that contains all the natural numbers, the value at any given index would be index+1
        - Now for a given sorted array of random positive integers, the number of positive integers that's missing in the array at any given index is arr[index] - (index+1) -> where index+1 is the value of the natural number that should be there if there was no misses before. 
        - This is pretty much what we're solving for in the algorithm. 
        - To understand the last return statement , I urge you to go through the first example array in the question and just writing the above logic out on a piece of paper. 
        - The condition for res === float('inf') is for cases when kth missing number comes before the first element of the array. Because in this case, the code never hits the else condition as arr[mid] - mid+1 will always be >= k. 

        Time Complexity: O(logn)
        Space Complexity: O(1)
        Reasoning : obv
        """

        low = 0
        high = len(arr) -1
        res = float('-inf')

        while low <= high:
            
            mid= (low + high) // 2

            if arr[mid] - (mid+1) >= k:
                high = mid-1
            else:
                if mid > res:
                    res = mid
                low = mid+1
        
        if res == float('-inf'):
            return k
        
        
        return arr[res] + (k - (arr[res] - (res+1)))