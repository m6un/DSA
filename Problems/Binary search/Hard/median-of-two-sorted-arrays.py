"""
Problem: Median of two sorted arrays 
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        - Interesting, LC Hard, so there would some enormous catch somewhere here. 
        - We need to return the median of the combined sorted array of the two given arrays. 
        - Where is binary search on answers coming here ?
        - TC should O(log(m+n)) -- interesting. So the binary search should be used to assemble the single sorted array from the two subarrays. 
        """

        n = len(nums1)
        m = len(nums2)

        # low = 0 
        # high = n + m - 1

        # arr_low = float('inf')
        # arr_high = float('-inf')

        # while low <= high:

        #     mid = (low + high) // 2

        #     if mid > n-1:
        #         value_of_mid = nums2[n-mid]
        #     else:
        #         value_of_mid = nums1[mid]

        if len(nums1) != 0 and len(nums2) != 0:
            low = min(nums1[0], nums2[0])
            high = max(nums1[n-1], nums2[m-1])
        
        elif(len(nums1) == 0):
            low = nums2[0]
            high = nums2[m-1]

        elif(len(nums2) == 0):
            low = nums1[0]
            high = nums1[n-1]

        median = (low + high) / 2

        return median

        """
         - wait, we know what the total number of elements gonna be. If it's odd - we just need to find the value at n+1 / 2 and if it's even we need to find the values at n/2 and n/2 +1 , maybe use binary search for that ?
         - Apparently we have to ideate in this direction: 
            - For a sorted array of size N, the left half would be of the size (N+1)/2 -> this is for both even and odd total number of elements in the array. 
            - Now, this left half could be composed of x elements from the first array and y elements from the second array such that x + y = N+1 / 2
            - Here, we do binary search on figuring out the x . We do binary search on x, now if we assume x to be of one value, we know y would be N+1 / 2 - x. That way we come to the perfect point somehow. 
        """