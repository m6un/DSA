"""
Problem: minimum number of days to make m bouquets
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""
class Solution:
    def minDays_partial_solve(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        bloomDay -> array which shows ith flower blooms on bloomsDay[i]
        m -> the number of bouquets you should make
        k -> The number of adjacent flowers you have to pluck to make 1 bouquet
        Return -> min number of days you need to wait to make m bouquets from the garden
        """

        """
        - Adjacency is important 
        - Think about how to reduce the search space ? -> if value // mid this shrinks the search space (no this is wrong. I mean it does but we need the shit. )
        - I need to find out how many adjacent k's are there. If that's >=m , I need to keep that as potentail result. And I need to find the lowest such value that I can find. 
        """

        low = 1 
        high = max(bloomDay)

        res = float('inf')

        while low <= high:
            mid = (low + high) // 2

            adjacent_flower_count = 0
            bouquets = 0 
            for j in range(len(bloomDay)-1):

                bloomed = bloomDay[j] / mid
                bloomed_next = bloomDay[j+1] / mid

                if k >1:
                    if adjacent_flower_count == k:
                        bouquets += 1
                        adjacent_flower_count = 0 
                                
                    if bloomed_next <=1 and bloomed <= 1:
                        adjacent_flower_count += 1
                    else:
                        adjacent_flower_count = 0
                else:
                    if bloomed <= 1:
                        bouquets += 1
            
            if k<=1 and bloomed_next <= 1:
                bouquets += 1
        
                
                print("adjacent flower count", adjacent_flower_count, "bouquets", bouquets, mid, "bloomed", bloomed, "bloomed_next", bloomed_next)
            
            
            if k > 1 and adjacent_flower_count == k:
                bouquets += 1 
        
            if bouquets < m:
                low = mid+1
            else:
                if mid < res:
                    res = mid
                high = mid-1
        
        if res != float('inf'):
            return res 
        
        return -1
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        """
        Intuition: 
        - This is a combined question -> Binary search on answers + Greedy algorithm. I kinda messed up and overcomplicated on the greedy algorithm in the previous solution. But I did get close. This would also act as a greedy algorithm revision for me. 
        - You can just do a simple pass and maintain a variable for calculating the streak.
        - streak resets in two scenarios:
            - When you encounter a flower that has not bloomed yet (breaking the adjacency).
            - When your streak hits k (because you've successfully bundled them into a bouquet and need to start counting fresh for the next one).
        - The reason why we call it greedy is because you're looking at the local maxima only. You're not grabbing the value and storing it for future use you deal with what you got at the moment and move on. That is how you're "Greedy"

        Time Complexity: O(Nlog(max(bloomDay)))
        Space Complexity: O(1)
        Reasoning : For TC -> N - length of the bloomDay array and for binary search, the length of the og search space is max(bloomDay) since we considered search space to be [1,...,max(bloomDay)]
        """
    
        low = 1 
        high = max(bloomDay)

        res = float('inf')

        while low <= high:
            mid = (low + high) // 2
            bouquets = 0
            streak = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    streak += 1
                else:
                    streak = 0
                
                if streak == k:
                    bouquets += 1
                    streak = 0
            
            if bouquets < m:
                low = mid+1
            else:
                if mid < res:
                    res = mid
                high = mid-1

        if res != float('inf'):
            return res 
        
        return -1