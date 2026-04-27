"""
Problem: Three sum
Difficulty: M
Link: https://leetcode.com/problems/3sum/
"""
class Solution:
    def threeSum_bruteforce(self, nums: list[int]) -> list[list[int]]:
        """
        Intuition: 
        Nothing much on the intuition , O(N^3) solution, the only thing is we can't duplicate triplets so I used set + a flag to know if we should break the loop and continue

        Time Complexity: O(N^3)
        Space Complexity: O(1) if result array not considered. IF considered then O(N2)
        Reasoning : The reasoning for SC is the degrees of freedom concept in Maths. we have : 
            a+b+c = 0 
            now, a+b can always be equal to -c. Which means we have the optionality to pick two distinct integers, making our degree of freedom 2. Now, mathematically, if you have to pick 2 distinct integers, the options are : 
            N(N-1) / 2 -> Which would be O((N^2 - N ) / 2) -> O(N^2)
        """
        result=[]
        arr_len = len(nums)
        for i in range(2,arr_len):
            for j in range(1,i):
                for k in range(j):
                    should_break = False
                    if nums[i]+nums[j]+nums[k] == 0:
                        # Here the thing is they don't want duplicate triplets. Meaning [-1,0,1] should be there but there shouldn't be [1,0,-1] or [-1,1,0]
                        for value in result:
                            if set(value) == set((nums[i],nums[j],nums[k])):
                                should_break = True
                        if should_break == True:
                            continue
                        else:
                            result.append([nums[i],nums[j],nums[k]])
        return result

        """
        The a