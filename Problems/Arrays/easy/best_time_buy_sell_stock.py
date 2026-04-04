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
    
    def optimal_solution(self, prices: List[int]) -> int:
        """
        Intuition: We pass through. And when we pass through, we keep two variables 
        1. Cheapest value - and check if the current value is the cheapest or not, if yes replace. 
        2. Compare the diff between the current value and the cheapest value seen so far and see if they beat your max profit variable -> this is the second variable. 
        
        I think the idea or what you need to think to work out such questions using a single pass is to remember key values from the past using variables and when you walk through you compare what you have with these key values and update accordingly. --> This should be the mental model imo. One pass optimizations work this way: 
        Update your best so-far as an when you discover new information.

        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning : obvious
        """
        max_profit = 0 
        cheapest_value = prices[0]
        for value in prices:
            if value < cheapest_value:
                cheapest_value = value
            elif value - cheapest_value > max_profit:
                max_profit = value - cheapest_value
        return max_profit
        