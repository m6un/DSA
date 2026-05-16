"""
Problem: Binary search
Difficulty: E
Link: https://leetcode.com/problems/binary-search/
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition: This is straightforward binary search recursive implementation 
            - You take the largest search space and progressively reduce it until you find your findable or until you shrink the search space to nothing. ( low > high invariant)

        Time Complexity: O(logn)
        Space Complexity: O(logn)
        Reasoning : reason for TC to be o(logn) is size of the recursion stack ( max possible ) x TC for one level, which here is just O(1). 
            It's interesting for SC - for SC it's o(logn) because of the recursion stack worst size. Now, there's an iterative variant also for binary search. I have written it in GoodNotes. using while loop. For that, the TC is still O(logn) , but the SC will be O(1)
            because it's not doing recursion. And interestingly, this iterative solution is also preferred in production systems!!
        """
        def recursive_s(low,high):
            if low > high:
                return -1 
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return recursive_s(low, mid-1)
            else:
                return recursive_s(mid+1, high)
        
        return recursive_s(0, len(nums)-1)