"""
Problem: Single number
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Intuition: There's no intuition here. It's plain theory of the XOR operator. For XOR, if you XOR a number with itself, only then it'll give you 0. And if you XOR a number with zero, it gives you that number. So basically we do one big XOR operation with the members of the entire array and you get the one that doesn't have a pair.

        Time Complexity: O(N)
        Space Complexity: O(1)
        Reasoning : obvious
        """
        start = nums[0]
        for i in range(1,len(nums)):
            start = start ^ nums[i]
        return start
        