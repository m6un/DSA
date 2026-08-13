class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Let's go , LC Hard. 
        - You've got the list nums
        - You've got the value k, you need to split nums into k non-empty subarray such that the largest sum of any subarray is minimized. 
        - I'm confused and tired, but we need to do this. 
        - Hmm...... 
        - How to conver this to a binary search for answers solution.... 
        - I mean I don't have to think about this as splitting into subarrays, but I can think of it as similar to grouping into adjacent groups right. 
        - I got some ideas from hermu yesterday, he said we'll have to think about solving this in nlogm time. so : 
        - low = min(nums)
        - high = sum(nums)
        - then for any value we'll have to greedily find out if we can form one adjacent group with that sum or something. 
        """

        low = min(nums)
        high = sum(nums)

        res = float('inf')

        while low <= high:

            mid = (low + high) // 2 #our sum

            temp_sum = 0 
            groups = 0 
            for i in range(len(nums)):

                temp_sum += nums[i]

                if temp_sum > mid:
                    temp_sum = nums[i]
                    groups += 1 # I'm not sure about this.
                elif temp_sum == mid:
                    # THis is tricky place. 
                    temp_sum = 0
                    groups += 1
                    """
                    What are my problems here ? 
                    - Major problems are:
                        - I don't know where to slot the check for k. In here, even if it matches, we need to know if including this group, we can form k groups. 
                        - I need to have some logic that I can use to modify low and high after each of these for loop ends. From walking through, I've understood that we may have to store the highest sum calculated here and if that's > mid we'll have to go high = mid-1 or low = mid+1. 
                    """








        
        