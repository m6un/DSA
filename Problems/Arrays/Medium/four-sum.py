"""
Problem: 4-sum
Difficulty: M
Link: https://leetcode.com/problems/4sum/
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        1. Unique quadruplets 
        2. 
        """
        # I think sorting here will help. Now what to do after sorting ? for 3 sum we needed 3 pointers. NOw for 4 sum we'll need 4 pointers. hmmm.... 

        #sort the array 
        nums.sort()
        arr_len = len(nums)
        result = []

        #hmm we've got a lot of sorted array privileges hmmm. 
        ref_map = {}

        for i in range(arr_len-3):

            if nums[i-1] == nums[i]:
                continue
            left = i+1 
            right = arr_len - 1
            while left < right:
                qsum = nums[i] + nums[left] + nums[right]
                if qsum in ref_map:
                    result.append([nums[i], nums[left], nums[right]])
                else: