"""
Problem: Max consecutive ones
Difficulty: Easy
Link: https://leetcode.com/problems/max-consecutive-ones/
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Intuition: quite straightforward

        Time Complexity: O(N)
        Space Complexity: O(1)
        Reasoning : NIL
        """
        max_count = 0 
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0 
            
            if count > max_count:
                max_count = count
        
        return max_count