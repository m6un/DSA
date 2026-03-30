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
    
    def optimal_solution(self, nums: List[int]) -> None:
        """
        Intuition: So this is an algorithm known as Dutch national flag algorithm. Instead of looping multiple times, we use "3 pointers" to partition the array in a single pass. 
        1. low: the boundary where the next 0 should go 
        2. mid: the current element we're inspecting
        3. high: the boundary where the next 2 should go 
        
        Some things that I noticed: 
        1.Low and high are like two walls that are moving in from the two sides and the mid pointer is what explores what’s in between
        2.Why we do not increment mid when a high value gets swapped into the mid’s position is because we don’t know what value that is. If it’s a zero then it needs to go into the front. Now, why doing the exact same thing in the low block instead of high doesn’t work is because our mid pointer itself starts from low. So it knows what’s there in the low block, but it’s the high block that’s unknown to it. 

        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning : one pass and no extra data structures used
        """

        #Dutch National Flag Algorithm
        arr_len = len(nums)
        low = 0
        mid = 0
        high = arr_len - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
            
            else: 
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1