"""
Problem: Majority element
Difficulty: Easy
Link: https://leetcode.com/problems/majority-element/
"""
class Solution:
    def brute_force_solution(self, nums: List[int]) -> int:
        """
        Intuition: Just use Hashmap - O(n) SC and TC 

        Time Complexity: O(n)
        Space Complexity: O(n)
        Reasoning : 
        """
        count_lookup = {}
        arr_len = len(nums)
        for i in range(arr_len):
            if nums[i] in count_lookup: 
                count_lookup[nums[i]] = count_lookup[nums[i]] + 1  
            else:
                count_lookup[nums[i]] = 1
            if count_lookup[nums[i]] > arr_len/2 :
                return nums[i]
    
    def optimal_solution(self, nums:List[int]) -> int:
        """
        Intuition: Boyer-Moore voting algorithm: 
        The idea is that since there's a number that's more than half the array length, It can "outvote" all other elements combined -- basically you just compare two elements and if they are not the same, they cancel out -- ELIMINATION BY PAIRING. 
        
        We maintain two variables - candidate and count. After a single pass, whatever elment is held by candidate variable will be the answer.
        
        TODO: Have to write proper intuition tomorrow.

        Time Complexity: O(n)
        Space Complexity: O(1)
        Reasoning : obv
        """
        count_1, count_2 = 0, 0
        cand_1, cand_2 = None, None
        for value in nums:
            if value == cand_1:
                count_1 += 1
            elif value == cand_2:
                count_2 += 1
            elif count_1 == 0:
                cand_1 = value 
                count_1 += 1
            elif count_2 == 0:
                cand_2 = value 
                count_2 += 1
            else:
                count_2 -= 1
                count_1 -= 1
        print(cand_1, cand_2)
        # return list({cand_1, cand_2})

        count_1 = 0 
        count_2 = 0
        result = []

        for value in nums:
            if value == cand_1:
                count_1 += 1
            elif value == cand_2:
                count_2 += 1
        if count_1 > len(nums) // 3:
            result.append(cand_1)
        if count_2 > len(nums) // 3:
            result.append(cand_2)
        return result