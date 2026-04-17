"""
Problem: Subarray Sum Equals K
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Intuition: 

        Time Complexity: O()
        Space Complexity: O()
        Reasoning : 
        """
        i = 0 
        count = 0 
        current_sum = 0 
        arr_len = len(nums)
        for j in range(arr_len):
            if nums[j] + current_sum > k:
                current_sum = 0
                i = j
            
            elif nums[j] + current_sum == k:
                count += 1
                current_sum = 0
                i = j