"""
Problem: Next permutation
Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Intuition:
            We're not supposed to return anything. This is an O(1) operation. 
            Lexicographic order means the dictionary order of things. The intuition here is to first understand that mostly we'll be dealing with parts of arrays that are sorted descending. This is because that's the highest value a particular permutation can have, as mentioned in the question description. 

            Intuition is to identify the first decreasing pair from the right ( i < i+1 ), keep the i as pivot, swap with the smallest value that's larger than pivot value, and then reverse nums[pivot+1:], because if you see the code, the part to the right of pivot will already be decreasingly sorted.
        Time Complexity: O(N)
        Space Complexity: O(1)
        Reasoning : SC is obvious. for TC, we're doing three disjointed loops here, but all of them add up to O(3n) which essentially is o(n) 
        """
        n = len(nums)
        pivot = -1

        # Now we check if there are any pairs from the right where nums[i] < nums[i+1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i 
                break
        
        # If pivot != -1 , we'll find the smallest value that's larger than pivot and swap them.  
        if pivot != -1:
            for i in range(n-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
        
        left, right = pivot+1, n-1 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums