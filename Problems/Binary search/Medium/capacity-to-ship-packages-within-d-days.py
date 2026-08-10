"""
Problem: Capacity to ship packages within d days
Difficulty: Medium
Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Intuition: 
        - Pretty much binary search + greedy algorithm. I think the key to solving such questions is to just nail the greedy part, because that's where the modifications come in the pattern.

        Time Complexity: O(NlogD , where D = sum(weights) - max(weights))
        Space Complexity: O(1)
        Reasoning : obv
        """
        
        low = max(weights)
        high = sum(weights)
        res = float('inf')

        while low <= high:

            mid = (low + high) // 2
            
            day_count = 0 
            total = 0 
            for i in range(len(weights)):

                if total + weights[i] > mid:
                    day_count+= 1
                    total = 0
                
                total += weights[i]
            
            if total != 0:
                day_count+=1
            
            if day_count > days:
                low = mid+1
            else:
                if mid < res:
                    res = mid
                high = mid-1

        return res