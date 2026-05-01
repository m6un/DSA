"""
Problem: 4-sum
Difficulty: M
Link: https://leetcode.com/problems/4sum/
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Intuition: Some ground breaking intuition I got from this problem : Use while loops only if you have a concrete constraint in your hand to handle the pointers or pointer. If you don't have it, just use a for loop. You use a while loop only to make a for loop situation more TC efficient. But you should only do that if you have a concrete constraint with which you can modify the pointer / pointers' places and make the traversal efficient by skipping unwanted elements. 
        
        Coming to this problem the intuition is that for 4sum - you need 4 pointers. You fix the 2 of them and then do a while traversal, similar to how you do in 3sum. 

        Time Complexity: O(N^3)
        Space Complexity: O(1 or N)
        Reasoning : SC is because python's built in sort function uses something called Time sort, which can have a worst case SC of O(N) -- something to look into later on. for knowledge hmmm. 
        """
        # I think sorting here will help. Now what to do after sorting ? for 3 sum we needed 3 pointers. NOw for 4 sum we'll need 4 pointers. hmmm.... 

        #sort the array 
        nums.sort()
        arr_len = len(nums)
        result = []

        for i in range(arr_len - 3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, arr_len - 2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                
                left = j+1
                right = arr_len -1
                while left < right:
                    q_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if q_sum < target:
                        left += 1
                    elif q_sum > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return result