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

    def optimal_solution(self, nums:List[int]) -> int:
        """
        Intuition: Boyer-Moore voting algorithm: 
        The idea is that since there's a number that's more than half the array length, It can "outvote" all other elements combined -- basically you just compare two elements and if they are not the same, they cancel out -- ELIMINATION BY PAIRING. 
        
        We maintain two variables - candidate and count. After a single pass, whatever elment is held by candidate variable will be the answer. 
        The above is true but with a caveat. In Majority Element II, unlike Majority Elmenet I, there is no guarantee that there'll be a winner / winners. 
        Boyer-Moore is fundamentally a destruction algorithm.
        - If a true majority element exists, it is mathematically too massive to be destroyed. It will absolutely survive the battle.
        - However, if no majority element exists (e.g., [1, 2, 3, 4, 5]), the algorithm doesn't magically return empty-handed. Somebody is still going to survive the battle simply by walking into the room last.
        Now, for the last case we have the final loop which checks if the ones survived are actually our winners or they just ended up walking into the room last. 
        
        Also here's the intuition for the order of the if-elif-else chain : Are you already on the list? -> No -> Is there an empty seat? -> No -> Okay, everyone takes damage.

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