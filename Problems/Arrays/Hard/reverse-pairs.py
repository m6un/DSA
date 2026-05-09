"""
Problem: Reverse pairs
Difficulty: H
Link: https://leetcode.com/problems/reverse-pairs/
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        Intuition: This is the first LC hard that I'm doing and it's a very interesting question. We're are using a divide-and-conquer algorithm , Merge sort to find out the reverse pairs. 
        - We're using the division to comply to i < j requirement and we're doing the sorting bit to make counting easier for us. 
        - I had this question of why sort, why not just divide, count and then merge back ? The problem with that is then we don't have any concrete backing to decide when to move the pointers. We split an array and then you have two completely unsorted subarrrays. and you keep a pointer at the left half and you keep a pointer at the right half. The problem with not having them sorted is that you donn't have a backing to move the pointers. 
        - Now if both the halves are sorted respectively: 
            - You point i at the start of left and j at the start of right. If you discover that left[i] > 2 * right[j], you don't just find one pair. Because the left array is sorted, you instantly know that every element after left[i] is also a valid pair with right[j]. 
            - You can add all of them to your count in a single $O(1)$ math operation, increment your j pointer, and move on.By having the halves sorted, you turn a nested $O(N^2)$ cross-comparison into a linear $O(N)$ sweep.   

        Time Complexity: O(NlogN)
        Space Complexity: O(N) (temp array max possible space - this is auxiliary space) + O(logN) ( recursion stack max depth space ) = O(N)
        Reasoning : reasoned.
        """
        def merge(low, mid, high):
            temp = []
            count = 0
            left = low
            right = mid+1
            
            while left <= mid and right <= high:
                # Trying this out - we're finding the count first. 
                if nums[left] > 2 * nums[right]:
                    count += ( mid - left + 1)
                    right += 1
                else: 
                    left += 1
            
            left = low 
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
                
            while left <= mid:
                temp.append(nums[left])
                left += 1 
                
            while right <= high:
                temp.append(nums[right])
                right += 1
            
            for i in range(low,high+1):
                nums[i] = temp[i - low]
            return count
            
        def count_sort(low,high):
            if low >= high:
                return 0
            mid = (low + high) // 2

            left_count = count_sort(low, mid)
            right_count = count_sort(mid+1, high)

            cross_count = merge(low, mid, high)
            return left_count + right_count + cross_count
        
        low = 0 
        high = len(nums) - 1

        return count_sort(low, high)