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
        j = 1
        count = 0 
        current_sum = 0
        arr_len = len(nums)
        if nums[i] == k:
            count+= 1
        while j < arr_len:
            current_sum = sum(nums[i:j+1])
            print(f"{i}{j}{count}{current_sum}")
            if current_sum == k:
                i = j 
                count += 1
                j+= 1
            elif current_sum < k:
                j+= 1
            else:
                i+= 1
        return count