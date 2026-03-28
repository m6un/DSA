"""
Problem: Two sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/
"""
class Solution:
    
    def brute_force_solution(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    
    def solution():
        """
        Intuition: So in the above brute force solution what we're doing is we fixed one value and we're "searching" for the next value. Now what we have to optimise for progressively is this "searching". A proposed train of thought here is to use "extra space" for optimising this search. And the answer for that is a HashMap. 
        - In Hashmaps the lookup is an O(1) operation , while in an array this is an O(n) operation. 
        - In the below code when we write if nums[i] in two_sum_map what happens in the bg is: 
            - python runs the hash function on nums[i] - O(1) time 
            - it gets an index ( eg. 5)
            - it looks at the 5th bucket in its internal memory 
            - If something's there it returns true if not false. 
        Here's the actual intuition behind the solution : 
            - Hashmap helps us with "search". If you have a value in hand, what are you searching for ? - (target - value)
            - If we keep that as a key in hashmap and the value of that key being the index of the corresponding *value* in the array. 
            - Now when you look, if there is a key corresponding to what you're searching for, you can return the answer - [current index position from where you're searching for, value of the key in the hashmap] 
            - If not you just save the corresponding key and value in the hashmap and moveon to the next index. 
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        Reasoning : reasong for space complexity being o(n) is that the number of items in the hashmap grows linearly with the number of items in the input list. -- hence, linear space
        """
        two_sum_map = {}
        for i in range(len(nums)):
            key_to_save = target - nums[i]
            if nums[i] in two_sum_map:
                return [i, two_sum_map[nums[i]]]
            
            two_sum_map[key_to_save] = i