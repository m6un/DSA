"""
Problem: Rearrange array elements by sign
Difficulty: Medium
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        Intuition: Nothing much, since the question said we don't have to do it in place, we need to create a new result array, initialise it with zeroes and have two pointers to track the last index of positive and negative numbers from the nums array.

        Time Complexity: O(n)
        Space Complexity: O(n)
        Reasoning : obv
        """
        arr_len = len(nums)
        p_index = 0 
        n_index = 1
        result_array = [0] * arr_len
        for value in nums:
            if value > 0:
                result_array[p_index] = value 
                p_index += 2
            
            elif value < 0 :
                result_array[n_index] = value 
                n_index += 2
        return result_array