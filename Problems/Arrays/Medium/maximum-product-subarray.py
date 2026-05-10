"""
Problem: Maximum product subarray 
Difficulty: M
Link: https://leetcode.com/problems/maximum-product-subarray/description/
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Intuition: Hmm so this is a variation of Kadane's algorithm, but considering the Mathematical intricacies that come with having to calculate the max product. This is a DP question it seems so we'll explore the DP intuition also here. 
        
        DP -> The mental model is to break down the current problem at hand into smaller, overlapping sub-problems and using the results of those subproblems to calculate the CURRENT RESULT 
        Two main pillars of DP explained in the context of this problem: 
        
        1. Optimal substructure: The optimal solution at the current index (i), is entirely reliant on the optimal solutions at the previous index. in this case - max_sf and min_sf at the previous index. The idea is you can't calculate the optimal solution at the current index
        without knowing the optimal solution of the previous index. 
        2. Overlapping subproblems: As we iterate through the array, we're continuously reusing the previously calculated max_sf and min_sf states to calculate the next state, rather than recalculating the products from the beginning of the array next time. 
        
        Here for this problem the specific intuition / what makes it a variation of the OG Kadane's algorithm is that : 
        1. This is product and that's sum. For product, since two negatives could give a positive, we can't only be bothered about the max sum at the point alone, we also need to keep another variable which keep tracks of the min product so far , which could later on beat the max product so far , if a negative value is encountered. 

        Time Complexity: O(N)
        Space Complexity: O(1)
        Reasoning : obv
        """
        max_sf = nums[0]
        min_sf = nums[0]
        res = nums[0]

        for value in nums[1:]:
            temp_max = max(value, value * max_sf, value * min_sf)
            min_sf = min(value, value * max_sf, value * min_sf)
            
            max_sf = temp_max
            res = max(res, max_sf)
            
        return res