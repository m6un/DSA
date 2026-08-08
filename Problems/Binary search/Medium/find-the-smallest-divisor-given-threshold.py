"""
Problem: Find the Smallest Divisor Given a Threshold
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
"""
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        Intuition: 
            - low = 1 <= divisor <= max(nums)

        Time Complexity: O(Nlog(max(nums)))
        Space Complexity: O(1)
        Reasoning : obv
        """

        low = 1 
        high = max(nums)
        res = float('inf')

        while low <= high:

            mid = (low + high) // 2

            total = 0
            for i in range(len(nums)):
                total += -(-nums[i] // mid)
            
            if total > threshold:
                low = mid+1
            else:
                if mid < res:
                    res = mid
                high = mid-1
        
        return res