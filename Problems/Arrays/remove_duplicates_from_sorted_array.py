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
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        I'm trying to think on how to do it first time, what's the first approach that's coming to my mind for solving this. Hmmmm.... WE need to walk, we need a pointer to walk from the first item. And then what? what will it compare the value with ? Hmm this is an array that's sorted in non-decreasing order. and we have to remove the duplicates in place. Hmm interesting. I've got an idea. But that's not really doing it in-place hmm. 
        """
        staging_array = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                staging_array.append(nums[i])
        return len(staging_array)
    
        


        
def test_solution():
    """Test cases"""
    # Test case 1
    assert solution() == expected_result
    
    # Test case 2
    # assert solution() == expected_result
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()