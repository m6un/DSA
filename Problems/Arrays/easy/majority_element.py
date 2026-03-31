"""
Problem: Majority element
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/
"""
class Solution:
    def brute_force_solution(self, nums: List[int]) -> int:
        """
        Intuition: Just use Hashmap - O(n) SC and TC 

        Time Complexity: O(n)
        Space Complexity: O(n)
        Reasoning : 
        """
        count_lookup = {}
        arr_len = len(nums)
        for i in range(arr_len):
            if nums[i] in count_lookup: 
                count_lookup[nums[i]] = count_lookup[nums[i]] + 1  
            else:
                count_lookup[nums[i]] = 1
            if count_lookup[nums[i]] > arr_len/2 :
                return nums[i]