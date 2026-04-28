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
    
    def threesum_hashmap_partial(self, nums: list[int]) -> list[list[int]]:
        arr_len = len(nums)
        result = set()
        ref_map = {}
        
        # Populate the map with the FIRST occurrence of each number
        for i in range(arr_len):
            if nums[i] not in ref_map:
                ref_map[nums[i]] = i

        for i in range(arr_len):
            for j in range(i):
                key = -(nums[i] + nums[j])
                
                # If the required 3rd number exists in our map...
                if key in ref_map:
                    # Make sure the 3rd number's index isn't the same as i or j
                    if ref_map[key] != i and ref_map[key] != j:
                        # Sort the triplet so permutations look identical, 
                        # cast to tuple, and add to the set.
                        result.add(tuple(sorted((nums[i], nums[j], key))))

        # Convert the set of tuples back to a list of lists before returning
        return [list(t) for t in result]