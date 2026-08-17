"""
Problem: Split array largest sum
Difficulty: Hard
Link: https://leetcode.com/problems/split-array-largest-sum/description/
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Intuition: 
        
        - This is an LC Hard and rightly so. 
        - The idea here is to : 
            - Set the search space - max(array) -- sum(array) - a subarray sum's min to max values. 
            - Now, once the groups are calculated, we check -> are the groups > k, that means the mid value that we have splits the array into more than k groups, which means the mid is small that it splits too much, we need mid to be high so low = mid+1
            - Else, which means that our mid managed to split the array into groups < k. Now this is an acceptable value, but we can do better - because we're looking for the minimum sum. 
            - A very interesting thing, that I'm yet to wrap my head around fully here is that the mid value which you find where your groups <= k and your mid is the lowest possible , is interestingly where your groups will be exactly equal to k. Now this is an implicit relationship , for which we're explicitly checking for. Check the code, the else loop is for groups <= k. That's what's been wrecking my head for sometime hmmm.... 
            - Got some more idea on the thing that's confusing me: 
                - The exact breaking point is guaranteed to be a real sum because for the array to be further split , only if we squeeze below the sum of the biggest subarray, you're guaranteed that there'll be a split. 
                - And we're always considering mid value to be the hypothetical maximum limit that no subarray should exceed. 
                    - During the binary search, mid is often just a loose upper bound. The actual largest sum of your groups might be lower than mid.
                    - It is only at the exact breaking point (the very end of the search) that this hypothetical limit is squeezed so tightly that mid perfectly equals the actual largest subarray sum.

        Time Complexity: O(NlogD), where D = sum(nums) - max(nums)
        Space Complexity: O(1)
        Reasoning : obv
        """
        low = max(nums)
        high = sum(nums)

        while low <= high:

            mid = (low + high) // 2 #our sum

            temp_sum = 0 
            groups = 1
            for i in range(len(nums)):

                temp_sum += nums[i]

                if temp_sum > mid:
                    temp_sum = nums[i]
                    groups += 1

            if groups > k:
                low = mid+1
            else:
                high = mid-1
        
        return low
            









        