"""
Problem: Koko eating bananas
Difficulty: Medium
Link: https://leetcode.com/problems/koko-eating-bananas/
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Intuition: This is absolute bonkers man! Honestly, first time solving such a question. The mental model to follow here is this: 
        - The search space for these questions are not given, it's not the given unsorted array. The search space is something that we have to form. In this case the search space to form is : [low = How much bananas can koko eat for a minimum in an hour (1 banana), high = Max how many bananas Koko has to eat to comfortably complete the bananas in the given time]
        
        - The biggest hack here is this search space is, in fact sorted. And our job is to find a value from this sorted space that fits the given criterion, which in this case is the lowest value -> lowest speed at which koko has to eat the bananas such that he can complete it within h. 
        
        - The is the right way to solve a problem where you can form a sorted answer space and also the problem follows the mathematical principle of Monotonocity. The principle is such that you have a set of values that are boolean True / False based on a criteria until a point and then the boolean flips. You need to find this point. 

        Time Complexity: O(NlogM)
        Space Complexity: O(1)
        Reasoning : 
        - TC -> M -> max(piles) you have your search space [1,..,M] so there are M values. Binary search TC - O(logM). but each search operation takes O(N) for the inner for loop. Hence O(N) * O(logM) = O(NlogM) 
        
        - SC -> obv
        """

        # find the lowest possible eating speed of Koko 
        low = 1

        #find the highest possible eating speed of Koko
        high = max(piles)

        res = float('inf')

        # now we have a search space and the principle of monotonicity applies here ( boolean true / false based on a criteria until a point and then the boolean flips )

        while low <= high:

            mid = (low + high) // 2

            total = 0 
            for value in piles:
                total += -(-value // mid)
            
            if total > h:
                low = mid+1
            elif total <= h:
                if mid < res:
                    res = mid
                high = mid-1
        return res