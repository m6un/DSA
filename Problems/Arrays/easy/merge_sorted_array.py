"""
Problem: Merge sorted array
Difficulty: E
Link: https://leetcode.com/problems/merge-sorted-array/
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Intuition: Difference between a Simulation algorithm and a Greedy algorithm :
        - A Simulation algorithm is one where your code tries to literally mimic a physical process or follow a very literal set of rules step-by-step, often tracking states that don't strictly need to be tracked for the final result.
        - A Greedy algorithm is a strategy where you make the "**locally optimal choice**" at every single step, without worrying about the big picture or what happens next, trusting that these local best choices will lead to the global best answer.
        
        In the context of the Merge Sorted Array reverse iteration, the greedy choice is this:
        - "I have an empty slot at the very back of the array. I want the absolute largest number possible to go there right now."
        At every single step of your while loop, you look at nums1[i] and nums2[j]. You "greedily" grab the larger of the two, shove it into last_filled, and immediately move to the next slot.

        Why it's Greedy (and not Simulation):
        - You don't care about what happens to the spot you just took the number from.
        - You don't clean it up or set it to 0.
        - You just greedily consume the largest available numbers from the backs of both arrays until one runs out.

        Time Complexity: O(m + n)
        Space Complexity: O(1)
        Reasoning : Why the TC is O(m+n) and not O(max(m,n)):
        This is because we have to go through every element of nums1 array and nums2 array, one element per iteration. You can see that in the logic, inside the while loop , in the if block and else block we're only reducing either j or i, not both. Which means at a time only one element from either of the arrays is getting processed and hence, the m + n
        """
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
        # After your while loop: -> This is particularly important because we may have i run out and j array left. That means there are still elements in j left that we need to place and now we'll have to run the below loop. I faintly remember a similar situation in one of the sorting algorithms - Merge sort - the merging logic in merge sort.
        while j >= 0:
            nums1[last_filled] = nums2[j]
            last_filled -= 1
            j -= 1