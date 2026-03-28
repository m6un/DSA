"""
Problem: Rotate Array
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-array/description/
"""
class Solution:
    def solution():
        """
        Intuition: 
            This should be an easy question if there is no constraint that we have to do it in place. Meaning O(1) space complexity. The intuition is to reverse the entire array and then see if we can reverse the parts of the array. So, what we actually have to do is to reverse the entire array plus reverse the two parts of the array partitioned by the value k , which is the number of rotations. 

        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning : Space complexity is covered. 
            Total TC} = O(n) + O(k) + O(n-k) 
            If you simplify that:
                {Total TC} = O(n + k + n - k) = O(2n) 
                In Big O notation, we drop constant coefficients (like the 2), which leaves us with: O(n)
        """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        switch_no = k%len(nums)
        if switch_no == 0:
            return nums
        
        self._reverse(0, len(nums)-1, nums)
        self._reverse(0, switch_no - 1, nums)
        self._reverse(switch_no, len(nums)-1, nums)


    def _reverse(self, left: int, right: int, arr: [int]) -> [int]:

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        