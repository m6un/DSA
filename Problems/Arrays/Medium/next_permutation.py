"""
Problem: Next permutation
Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            We're not supposed to return anything. This is an O(1) operation. 
            Lexicographic order means the dictionary order of things. 
        """
        arr_len = len(nums)

        def bubble_sort(start_index):
            i = arr_len - 1
            while i > 0:
                j = start_index
                while j < arr_len - 1:
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
                i -= 1
        
        def is_descending(arr):
            for j in range(len(arr) - 1):
                if arr[j+1] > arr[j]:
                    return False
            return True
        
        if arr_len <= 2 or is_descending(nums):
            bubble_sort(0)
            return nums
        
        k = arr_len - 3
        while k >= 0:
            # I think the bigger question here is how do you know to decrement k ? as in how do you know that there is no lexicographically greater arrangement to the right of k ? I mean if it's sorted descending, then we know that there is no more way right.
            i = k + 1
            if is_descending(nums[i:]):
                k -= 1
                continue
            bubble_sort(i)
            nums[i], nums[i+1] = nums[i+1], nums[i]
            return nums