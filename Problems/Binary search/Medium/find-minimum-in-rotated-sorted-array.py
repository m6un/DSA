"""
Problem: Find minimum in rotated sorted array
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Intuition: 

        Time Complexity: O(logn)
        Space Complexity: O(1)
        Reasoning : 
        - Uhh sorted array, finding a value within it -> Immediate lock in on binary search 
        - Here we need to be creative because we're not dealt with a value. We need to find a value that's conditional / unique to the given array - here it's the lowest element in the array 
        - The mental model to keep in mind here, is aggressive elimination. We pick the zone that's fully sorted, we pick the single piece of useful information for us from there ( the local minimum ) and then we immediately shrink the search space by 50% to go hunt on the remaining territory. 
        """
        low = 0 
        high = len(nums) - 1
        lowest_value = float('inf')

        while low <= high:

            mid = (low + high) // 2

            if nums[low] <= nums[mid]:
                if lowest_value > nums[low]:
                    lowest_value = nums[low]
                low = mid + 1
            
            else:
                if lowest_value > nums[mid]:                
                    lowest_value = nums[mid]
                high = mid - 1
        return lowest_value