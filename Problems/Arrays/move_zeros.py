"""
Problem: Move zeroes
Difficulty: Easy
Link: https://leetcode.com/problems/move-zeroes/
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Intuition: We are supposed to modify the list in place. So initially I made some mistakes, at first I got the thing working with a brute force solution - but that was sub-optimal of course. I'll be sharing it here. For the bruteforce, I'm using an unwanted outer while loop. And what this did was it had the inner loop running everytime there was a zero found. THat's what made it sub-optimal. Now the optimal solution is we do one traversal. We keep one slow pointer, to keep track of the "first" zero you find. So the slow pointer moves such that it'll stop whenever it finds the first zero and then only moves if the fast pointer finds a non-zero. Then it swaps the zero with the non-zero value and then moves forward until it finds the next zero value. 

        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning : TC is because we're doing one traversal throughout the array in any case. Fast pointer will visit all the indexes.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

                slow += 1
    
    def brute_force_moveZeroes(self, nums: List[int]) -> None:
        i = 0 
        j = 0 
        while i < len(nums) - 1:
            if nums[i] == 0:
                for j in range(i,len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
            
            i += 1