"""
Problem: Merge Intervals
Difficulty: M
Link: https://leetcode.com/problems/merge-intervals/
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # brutttee force. 
        arr_len = len(intervals)
        result = []
        for i in range(arr_len-1):
            left_final, right_final = intervals[i][0], intervals[i][1]
            for j in range(i+1,arr_len):
                left_array = None
                right_array = None
                if left_final < intervals[j][0]:
                    left_array = [left_final, right_final]
                    right_array = intervals[j]
                else:
                    left_array = intervals[j]
                    right_array = [left_final, right_final]
                if left_array[1] >= right_array[0]:
                    left_final, right_final = left_array[0], right_array[1]
                    break
            result.append([left_final, right_final])
        
        return result