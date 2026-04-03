"""
Problem: best time to buy and sell stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
class Solution:
    def brute_force_solution(self, prices: List[int]) -> int:
        """
        Intuition: Just pass through each element twice.

        Time Complexity: O(n2)
        Space Complexity: O(1)
        Reasoning : 
        """
        arr_len = len(prices)
        max_profit = 0
        for i in range(arr_len):
            for j in range(i,arr_len):
                if prices[j] > prices[i]:
                    max_profit = max(max_profit, prices[j] - prices[i])
        
        return max_profit