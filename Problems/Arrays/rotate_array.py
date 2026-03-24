"""
Problem: Rotate Array
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-array/description/
"""
class Solution:
    def solution():
        """
        Intuition: 

        Time Complexity: O()
        Space Complexity: O()
        Reasoning : 
        """
    
    #trial - 1 - dumb solution - in progress
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(k):
            i = 0
            j = nums[i]
            nums[i] = nums[len(nums) - 1]
            while i < len(nums):
                i +=1
                nums[i] = j
        
        