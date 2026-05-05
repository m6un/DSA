"""
Problem: Merge Intervals
Difficulty: M
Link: https://leetcode.com/problems/merge-intervals/
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Intuition: Some learnings here : 
        1. When should you sort / modify the i/p to get to your answer ? 
        - Is the problem order independent ? 
        - Does the math checkout ? ( O(nlogn) tax of the i/p sorting , in case of sorting , other tax incase of other operation ) -- as in if the bruteforce TC is > the total TC that comes with the added tax of nlogn sorting. 
        - Am I looking for grouping ? Proximities ? or overlaps ? 
        
        ---> If you see a problem and realise the order doesn't matter, notice that the bruteforce is O(n^2) or worse, and see if you're looking for pairs/overlaps -> hit the i/p with the sort()
        
        ---> Order doesn't matter and modifying i/p would help solve it in lesser TC than bruteforce -> modify the input. 

        Time Complexity: O(nlogn)
        Space Complexity: O(n) 
        Reasoning : SC - O(n) because of the sorting technique (Timsort in python native sort) - at worst case will have O(n) auxiliary SC. 
        """
        arr_len = len(intervals)
        result = []
        intervals.sort()
        if arr_len == 1:
            return intervals
        last_processed = intervals[0]
        for i in range(1,arr_len):
            """
            How the logic should be is - it should be such that : 
            1. You maintain a last_processed variable. 
            2. You have the current element. You check if you can extend the last_processed array or not 
            3. If not you push the last_processed variable into result array and set the current element as last_processed. 
            """
            if last_processed[1] >= intervals[i][0]:
                right_bound = None
                if intervals[i][1] > last_processed[1]:
                    right_bound = intervals[i][1]
                else:
                    right_bound = last_processed[1]
                last_processed = [last_processed[0], right_bound]
            else:
                result.append(last_processed)
                last_processed = intervals[i]
        result.append(last_processed)
        return result