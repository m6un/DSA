"""
Problem: Remove Duplicates from Sorted Array
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution:   
    def removeDuplicates_trial_2_success(self, nums: List[int]) -> int:
        """
        Intuition: We've used two-pointer approach here to solve the problem.The idea is we have I, which starts at 0, and J, which starts at the next to I. It's more or less like the runner method or the runner        approach to group by. I would be keeping track of the sorted unique elements one by one by their position. J would be looking to skip the duplicates, find the next unique element, and then you skip I to the next next index. You just replace whatever value that is there with the next unique, and that's how you go forward. In the end, you just return I plus one, which would be the count of the array or the count of unique elements in the array.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning: 
        Time Complexity O(n): j starts at 1 and increments every iteration until len(nums) — touches every element exactly once. i only moves when a new unique is found but doesn't add iterations. Single pass = O(n). 
        
        Space Complexity O(1):No extra data structures; i and j are just integer indices (constant space) and in-place writes reuse the existing array.
        """
        # staging_array = [nums[0]]
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         staging_array.append(nums[i])
        # nums = staging_array
        # # return len(staging_array)

        #seems like we have to employ two-pointer approach here. One that would keep track of the current element in the original array and another one for just the unique elements. Not clear lol. Let me try, one solution is forming in my head hmmm.
        i = 0
        j = 1
        while j < len(nums): # need to think of the edge case here where j becomes len(nums) -- which is when all the end values are equal, in which case we're good. so not an edge case. 
            if nums[j] != nums[i]:
                i = i+1
                nums[i] = nums[j]
            j+=1   
        return i+1
    