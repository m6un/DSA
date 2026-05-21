"""
Problem: Find First and Last Position of Element in Sorted Array
Difficulty: M
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
class Solution:
    def searchRange_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition: The only problem here is since there is two seperate walks to the left most and right most ends, this is an O(n) solution and what we want is an O(logn) solution. And for that what's needed is for left and right walks, we have to do two seperate binary searches lmao -- See , the mental model that you have to follow is just this -- searching in an already sorted space -- ALWAYS THINK OF BINARY FUCKING SEARCH. SAY THE NAME -- BINARY FUCKING SEARCH -- THAT"S GODDAMN RIGHT!!

        Time Complexity: O(n)
        Space Complexity: O(logn) -- recursive stack size 
        Reasoning : 
        """
        def recursive_s(low, high):
            if low > high:
                return [-1, -1]
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                print(low, mid, high)
                left = mid
                right = mid
                # right walk :

                for i in range(mid+1,high+1):
                    if nums[i] != target:
                        right = i-1
                        break
                    else:
                        right = i

                
                #left walk:
                for i in range(mid-1, low-1, -1):
                    if nums[i] != target:
                        left = i+1
                        break
                    else:
                        left = i
                
                return [left, right]
            
            elif nums[mid] > target:
                return recursive_s(low, mid-1)
            else:
                return recursive_s(mid+1, high)
        
        return recursive_s(0, len(nums) - 1)