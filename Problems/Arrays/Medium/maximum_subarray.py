"""
Problem: Maximum subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def brute_force_solution(self, nums: List[int]) -> int:
        """
        Intuition: Nothing much, find all possible sub-arrays, find the max sum. 

        Time Complexity: O(n3) *lol*
        Space Complexity: O(1)
        Reasoning : We have a nested loop to one level + the sum method which again does a complete traversal. We can make it O(n2) by not computing the sum, but keeping a sub-array_sum variable for the inner j loop, because we're only adding the next value that comes to the existing sum that we know. No need to calculate sum every time. 
        """
        i = 0 
        arr_len = len(nums)
        max_sum = float('-inf')
        if arr_len == 1:
            return nums[0]
        for i in range(arr_len):
            j = i
            while j < arr_len:
                subarray_sum = sum(nums[i:j+1])
                if subarray_sum > max_sum:
                    max_sum = subarray_sum
                j+=1
        return max_sum