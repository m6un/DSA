"""
Problem: Majority element II
Difficulty: M
Link: https://leetcode.com/problems/majority-element-ii/
"""
class Solution:
    def brute_force_solution(self, nums: List[int]) -> List[int]:
        """
        Intuition: bruteforce - O(n) + hashmap 

        Time Complexity: O(n)
        Space Complexity: O(n)
        Reasoning : TC is interestingly O(n) here and not O(n^2) even if there is an inner loop of "not in result" , because it's always bounded. Mathematically, there can atmost be only 2 elements that satisfy the criteria that the floor of it's number of occurence in the array will be greater than n/3. because: 
        - If one element appears more than 1/3 of the time, it takes up, say, 34% of the array.
        - If two elements appear more than 1/3 of the time, they take up at least 34% + 34% = 68% of the array. 
        - This leaves 32% of the array for any other numbers.If you tried to have three elements that each appear more than 1/3 of the time, they would require at least 34% + 34% + 34% = 102% of the array.
        """
        ref_map = {}
        arr_len = len(nums)
        result = []
        for i in range(arr_len):
            if nums[i] in ref_map:
                print(nums[i])
                ref_map[nums[i]] = ref_map[nums[i]] + 1
            else:
                ref_map[nums[i]] = 1
            count = ref_map.get(nums[i],0)
            if count > arr_len // 3 :
                if nums[i] not in result:
                    result.append(nums[i])
        return result