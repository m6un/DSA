"""
Problem: Search in rotated sorted array
Difficulty: M
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution:
    def search_wrong_soln(self, nums: List[int], target: int) -> int:
        """
        - Hmm this is interesting. so the nums array is possibly rotated at a random index. and we have to find the target value from the output. This is yet another modification-ish question on the normie binary search. 
        - What I think we'll do binary search to find out the pivot first. 
        """

        low = 0 
        high = len(nums) - 1

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while low <= high:
            mid = ( low + high ) // 2
            if nums[mid] > nums[mid+1]:
                if (( target < nums[mid] and target > nums[0] ) or ( target == nums[mid] ) or ( target == nums[0] )):
                    print("left")
                    # target is in left sub-array.
                    low_left = 0
                    high_left = mid

                    while low_left <= high_left:
                        mid_left = ( low_left + high_left ) // 2

                        if nums[mid_left] == target:
                            return mid_left 
                        elif nums[mid_left] > target:
                            high_left = mid_left - 1 
                        else:
                            low_left = mid_left + 1 
                    return - 1

                if (( target > nums[mid+1] and target < nums[len(nums) - 1] ) or (target == nums[mid+1]) or (target == nums[len(nums)-1])):
                    print("right")
                    #target is in right sub-array. 
                    high_right = len(nums) -1 
                    low_right = mid + 1
                    
                    while low_right <= high_right:
                        mid_right = ( low_right + high_right ) // 2

                        if nums[mid_right] == target:
                            return mid_right 
                        elif nums[mid_right] > target:
                            high_right = mid_right - 1 
                        else:
                            low_right = mid_right + 1 
                    return - 1
                return -1
            
            else:
                high = mid - 1

        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1


# My assumption that you always have to go backward, i.e in the else block just giving high = mid - 1 is wrong. Apparantly you can solve this in one loop using the standard binary search and I have no idea how that's done but we'll look at it tomorrow. 
        