"""
Problem: Search in rotated sorted array II
Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""
class Solution:
    def search_partial(self, nums: List[int], target: int) -> bool:
        """
        - Treat this as a mental gym dude, we've got a loooong way to go my brother. hmmmm.... 
        - So this is search in rotated array part 2 , I kinda don't remember part 1 lolol 
        - Hmm this is literally the same search in rotated sorted array, but that there could be duplicates. , like non-distinct values hmm...
        - I need to understand that in this situation how does the thingy break, or how does the part 1 logic break.  

        """
        low = 0 
        high = len(nums)-1

        while low <= high:
            mid = ( low + high ) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[low] <= nums[mid]:

                if nums[low] == target:
                    return True
                
                if target > nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[high] == target:
                    return True
                
                if target > nums[mid] and target < nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        
        return False

        """
        The problem with having duplicates is that there could be situations with low == mid == high, and also then you would mistakenly consider one half being sorted, when it's not. 
        So does it mean that we can't use binary search anymore since there could be no situation when one half is always sorted ? Idtso. There could be some trick that can be employed. 
        """