"""
Problem: Kth Missing positive number
Difficulty: Easy
Link: https://leetcode.com/problems/kth-missing-positive-number/description/
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Doesn't feel to me like an easy question tbh. How to translate this to binary search for answers ? 
        - The major question here is how would you define the ceiling ? I mean I get it, how to define the ceiling. 
        """

        count = 0
        for i in range(1,max(arr)+1):

            low = 0
            high = len(arr) -1

            inner_res = self.inner_binary_loop(low, high, i, arr)

            
            if inner_res == -1:
                count+=1
                if count == k:
                    return i
        
        return max(arr) + (k-count)
        
    def inner_binary_loop(self, low, high, i, arr):

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] > i:
                high = mid-1
            elif arr[mid] < i:
                low = mid+1
            else:
                return arr[mid]
        
        return -1