"""
Problem: Reverse pairs
Difficulty: H
Link: https://leetcode.com/problems/reverse-pairs/
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Hmm weird, what's the catch here ? idk. 
        """
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    count += 1
        return count
        # The above is bruteforce, now we need to improve on this. Maybe to a o(n) solution ?one single pass ? 
        # Throw a hashimapo at it ? 
        """
        - Nah this is not a hashmap solution my brother. This is something else entirely. hmmm, i'll come back to this solution tomorrow , but I think we're good with the bruteforce solution for today and I'm happy that I moved this to the night. I'm enjoying solving these questions and I'm glad. 
        """
        r_map = {}
        for i in range(len(nums)):
            if i in r_map: