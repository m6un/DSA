"""
Problem: Subarray Sum Equals K
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
class Solution:
    def subarraySum_bruteforce(self, nums: List[int], k: int) -> int:
        """
        Intuition: Nothing much, we're iterating through the array a couple of times and there's also the sum function which makes it even worse. 

        Time Complexity: O(n3)
        Space Complexity: O(1)
        Reasoning : TC reasoning is in the intuition
        """
        for i in range(arr_len):
            if nums[i] == k:
                count += 1
            for j in range(i):
                current_sum = sum(nums[j:i+1])
                if current_sum == k:
                    count += 1
                
        return count

    def subarraySum_optimal(self, nums: List[int], k: int) -> int:
        """
        Intuition: This is a very mathematical algo imo. So the idea is this: 
            Let P[x] ( a prefix sum) be the sum of all elements of an array from 0 to index x. If you want to find the sum of a subarray that starts at the index i to your current index at j would be: 
            subarraySum = P[j] - P[i-1] -- Here i - 1 is the catch. Try to visualise the sum, you'll get the idea. 
        
        Now, about the intuition used for the Algo, in the above equation, think about what all info we have. We can have the sum upto an index. we can also have the difference value which is k. What we have to find is the P[i-1]. To find this out, we are using a map such that we can find all the possible sums before our current index, which we can substract from the sum upto our current index to get k. And we'll add that to count. 

        Time Complexity: O()
        Space Complexity: O()
        Reasoning : 
        """
        curr_sum = 0
        # We do this to catch the edge case that if the first element itself will be one of the count increasers. like [k] eg. nums = [3,2], k = 3. 
        # Mathematical explanation , if the current index is 0 , what is the sum upto the current index that we can remove to get to k ? It's 0. That is also why we keep 0:1. 
        prefix_sums = {0:1} 
        for num in nums:
            curr_sum += num

            #check if curr_sum - k exists in the map 
            if curr_sum - k in prefix_sums:
                count += prefix_sums[curr_sum - k]
            
            # update the map with the current prefix sum 
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        return count