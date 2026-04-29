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
    
    def threesum_sorted_two_pointer_full(self, nums: list[int]) -> list[list[int]]:
        """
        Intuition: The core problem with your previous approaches was that the numbers were in a random order, forcing you to use extra memory (a hash map) to find the missing piece, and extra processing (a set) to avoid duplicates.If we sort the array first, we gain two massive superpowers:
        - Duplicate Control: All identical numbers are now grouped right next to each other. If we evaluate a number and then see the exact same number right next to it, we can just skip it. No set() needed.
        - Directional Searching (Two Pointers): Think of this as turning 3Sum into a "Two Sum II" problem. We loop through the array, picking a target number a. We then need to find two remaining numbers, b and c, that add up to -a.
            - Because the array is sorted, we can place a left pointer right after a (pointing at the smallest available number) and a right pointer at the very end of the array (pointing at the largest available number).
            - If a + b + c is too small (less than $0$), we move the left pointer up to get a bigger number.If a + b + c is too big (greater than $0$), we move the right pointer down to get a smaller number.
            - If it equals $0$, we record it, then shift both pointers inward (skipping duplicates along the way).

        Time Complexity: O(N^2)
        Space Complexity: O(1 or N)
        Reasoning : SC is because python's built in sort function uses something called Time sort, which can have a worst case SC of O(N) -- something to look into later on. for knowledge hmmm. 
        """
        nums.sort()
        result = []

        for i in range(arr_len - 2):
            # at first we skip the duplicates if any. 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # a small optimization -- if the smallest number > 0, then there's no point in continuing. 
            if nums[i] > 0:
                break #break and continue because this is a sorted array. if the smallest >0 then no sums add up to zero here. 
            left = i + 1
            right = arr_len - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]

                if total_sum > 0:
                    #total sum > 0 , which means we have to decrement the right. to get a lower sum 
                    right -= 1
                elif total_sum < 0:
                    # increment left 
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    #shift pointers inward to look for next potential candidate 
                    left += 1
                    right -= 1

                    #skip duplicates in the process. 
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1

        return result