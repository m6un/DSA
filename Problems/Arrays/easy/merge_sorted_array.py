"""
Problem: Merge sorted array
Difficulty: E
Link: https://leetcode.com/problems/merge-sorted-array/
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Here's my thought we'll keep one pointer each for the two arrays. And what we'll do is : 
        1. we'll check which of the pointer's values are smaller. 
        2. If i ( nums1 ) is smaller, we increment i and continue 
        3. If j ( nums2 ) is smaller, we'll swap nums2[j] with nums1[i] and then put nums1[i] to the first zero which would be m+1th element in the nums1 array. and we'll need another pointer to keep track of this as well ig. 
        # """
        # k = m
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] > nums2[j]:
        #             nums1[k] = nums1[i]
        #             nums1[i], nums2[j] = nums2[j], nums1[i]
        #         else:
        #             nums1[k] = nums2[j]
        #         k+= 1
        #         print(nums1)
        
        # Hmm I'm not giving enough thougt to the fact that both the arrays are sorted increasing order hmmm...... 
        i = m-1 
        j = n-1 
        last_filled = len(nums1) - 1
        while j >= 0 and i >= 0:
            if nums2[j] > nums1[i]:
                nums1[last_filled] = nums2[j]
                last_filled -= 1
                j -= 1
            else:
                nums1[last_filled] = nums1[i]
                i -= 1
                last_filled -= 1
        # After your while loop:
        while j >= 0:
            nums1[last_filled] = nums2[j]
            last_filled -= 1
            j -= 1