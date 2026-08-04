"""
Problem: [Single element in a sorted array]
Difficulty: [Medium]
Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
class Solution:
    def singleNonDuplicate_bf(self, nums: List[int]) -> int:
        """
        1. sorted array -> only integers where every element appears exactly twice. 
        2. One element only appears once -> return that
        ----
        - Sorted array , finding a number -> binary search 
        - What modification in the logic ? -> 
        - Binary search -> means you have to reduce the search space . How do you reduce the search space here ? The core invariant here is that we have one non-repeating element , just one element that's not in a pair. I think we have to think about brute force here. 
        """
        # Brute force 

        low = 0 
        high = len(nums) - 1

        while low < high:
            pivot = (low + high) // 2

            #what if pivot is the non-repeating element ? 
            if nums[pivot-1] and nums[pivot-1] != nums[pivot]:
                if nums[pivot+1] and nums[pivot+1] != nums[pivot]:
                    return nums[pivot]
            
            if not nums[pivot-1] and nums[pivot] != nums[pivot+1]:
                return nums[pivot]
            
            if not nums[pivot+1] and nums[pivot] != nums[pivot-1]:
                return nums[pivot]
            
            # I think we're done with the edge cases with Pivot

            left_half = nums[low:pivot]
            right_half = nums[pivot+1:high+1]

            if len(left_half) != 1 and len(set(left_half)) % 2 != 0:
                high = pivot-1
            elif len(right_half) != 1:
                low = pivot+1
            print(left_half, right_half, low, high)
        
        return -1
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Intuition: This is a very mathematical one. The pairs that occur before the non-pair single element, will always have their first elements' index to be an even number. But after the single element, it disrupts the flow that all the pairs after, they start with odd index. We use this to discard left / right part of the pivot ( reduce search space , the core idea behind binary search ). 
        We'll only check the immediate left / right values of the pivot and we also know the index of the pivot. rest you can pick up from the code. 
        
        Time Complexity: O(logn)
        Space Complexity: O(1)
        Reasoning : obv
        """

        low = 0 
        high = len(nums) - 1

        while low <= high:

            pivot = (low + high ) // 2
            print(pivot, pivot%2)

            if pivot % 2 != 0:
                if pivot-1 >= 0 and nums[pivot-1] == nums[pivot]:
                    low = pivot+1
                
                elif pivot+1 < len(nums) and nums[pivot+1] == nums[pivot]:
                    high = pivot-1
                
                else:
                    return nums[pivot]
            
            else:
                if pivot-1 >= 0 and nums[pivot-1] == nums[pivot]:
                    high = pivot-1
                
                elif pivot+1 < len(nums) and nums[pivot+1] == nums[pivot]:
                    low = pivot+1
                
                else:
                    return nums[pivot]