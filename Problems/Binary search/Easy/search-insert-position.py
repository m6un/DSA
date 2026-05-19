"""
Problem: Search insert position
Difficulty: E
Link: https://leetcode.com/problems/search-insert-position/description/
"""
class Solution:
        """
        Intuition: I mean it's just binary search, but the key intuition here is returning low, in both the cases. 
        Two scenarios: 
        Scenario 1: The target is greater than the element at mid
        - You need to insert the target after this current element.
        - The algorithm triggers low = mid + 1.
        - The crossover happens (low is now greater than high).
        - Because the target belongs right after the element you just looked at, mid + 1 is the perfect insertion index. Since low was just updated to mid + 1, returning low is correct.
        
        Scenario 2: The target is less than the element at mid
        - You need to insert the target exactly at this current position, pushing the current element (and everything after it) to the right.
        - The algorithm triggers high = mid - 1.
        -The crossover happens (low is now greater than high).
        - Because the target belongs at the spot you were just looking at, mid is the perfect insertion index. Since high moved but low stayed exactly where it was at mid, returning low is correct.
        
        Why not high?
        When the pointers cross ( low > high ) they essentially swap their roles relative to the target. 
        1. low -> Now low becomes the lowest element that's greater than the target. Now, if we're to introduce a new value we should introduce it here and push all the other elements to right
        2. High -> high becomes the last element that's strictly less than target. And this is not where we want to insert our target. 

        Time Complexity: O(logn)
        Space Complexity: O(1 / logn)
        Reasoning : obv -- O(logn) for iterative solution is because in each iteration we're halving the array. hence log(n) to the base 2 iterations. Now, in each iteration we do O(1) work hence -> O(logn)
        """
        def searchInsert_recursive(self, nums: List[int], target: int) -> int:

            def recursive_s(low, high):
                if low > high:
                    return low
                
                mid = ( low + high ) // 2

                if nums[mid] == target:
                    return mid 
                
                if nums[mid] > target:
                    return recursive_s(low,mid-1)
                else:
                    return recursive_s(mid+1, high)
            
            return recursive_s(0, len(nums)-1)
        

        def searchInsert_iterative(self, nums: List[int], target: int) -> int:
            low = 0 
            high = len(nums) - 1

            while low <= high:
                mid = ( low + high ) // 2 

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return low