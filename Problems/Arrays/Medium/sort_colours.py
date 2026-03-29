"""
Problem: Sort colours
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/
"""
class Solution:
    def solution():
        """
        Intuition: 

        Time Complexity: O()
        Space Complexity: O()
        Reasoning : 
        """
    
    def brute_force_solution(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Okay so a brute force way that I can think of is 2 passes and for each pass we'll respectively swap the 0s , 1s into their right positions. This would swap the 2s into their right position as well automagically.
        arr_len = len(nums)
        i = 0
        for k in range(2):
            for j in range(arr_len):
                if nums[j] == k:
                    nums[i], nums[j] = nums[j], nums[i]
                    i +=1
        
        return nums