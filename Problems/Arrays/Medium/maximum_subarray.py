"""
Problem: Maximum subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def brute_force_solution(self, nums: List[int]) -> int:
        """
        Intuition: Nothing much, find all possible sub-arrays, find the max sum. 

        Time Complexity: O(n3) *lol*
        Space Complexity: O(1)
        Reasoning : We have a nested loop to one level + the sum method which again does a complete traversal. We can make it O(n2) by not computing the sum, but keeping a sub-array_sum variable for the inner j loop, because we're only adding the next value that comes to the existing sum that we know. No need to calculate sum every time. 
        """
        i = 0 
        arr_len = len(nums)
        max_sum = float('-inf')
        if arr_len == 1:
            return nums[0]
        for i in range(arr_len):
            j = i
            while j < arr_len:
                subarray_sum = sum(nums[i:j+1])
                if subarray_sum > max_sum:
                    max_sum = subarray_sum
                j+=1
        return max_sum
    
    def optimized_solution(self, nums: List[int]) -> int:
        """
        Intuition: This is what's called Kadane's algorithm. So, in the brute force, we were going through the same element thrice imo. But we needed to reduce it to just once. And for that we can consider a set of questions we can ask an element once we reach it : 
        1. Should we add this element to our sub-array ? 
        2. Should we throw our sub-array away, consider the new sub-array starting from here ?
        And to answer this, we can use the question of : 
        -> What happens to my current subarray sum if I add this number to it. If it's positive still, then that's helpful to us. But if it's going negative, we might as well reset our sum to zero, and start again. 
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning: obvious
        """
        
        max_sum = float('-inf')
        current_sum = 0
        for value in nums:
            current_sum += value 

            if current_sum > max_sum:
                max_sum = current_sum 
            
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
    
    def recursive_follow_up_partial_solution(self, nums: List[int]) -> int:
        """
        Intuition: This is not the complete solution. Here we're recursively splitting the array into to halves. And returning once we split them into single element array. 
        On top of that we're also calculating the sum of these split arrays as well. Now, in the end we return the maximum of these 4. Now, this is not complete and this is not at all optimal, why it's not complete is because this is not considering the case where there can be a sub-array that's spread across the center. That's not being considered here. 

        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        Reasoning : 
        TC O(nlogn) because total TC = (work per level) * (number of levels) = O(n) * logn. This is because at each level of the tree we're still doing a total of O(n) work, if you visualize the stack , the work being calculating the sum of each of the half. 
        SC O(n), ideally it should've been the height of the stack - O(logn), but here we are slicing the array. In python, when you slice an array, it creates new copies of them. So in the first step, when you slice - you get two new arrays of size n/2 and the old one of size n in the stack. This would be peak space = O(n/2) + O(n/2) + o(n) = o(2n) = O(n) 
        
        """
        arr_len = len(nums)
        def max_subarray_sum(self, low, high):
            if low >= high:
                return nums[low]
            med = (low + high)//2
            
            left_best = max_subarray_sum(self, low, med)
            right_best = max_subarray_sum(self, med+1, high)
            left_sum = sum(nums[low:med+1])
            right_sum = sum(nums[med + 1:high+1])
            return max(left_sum, right_sum, left_best, right_best)

        return max_subarray_sum(self, 0, arr_len-1)