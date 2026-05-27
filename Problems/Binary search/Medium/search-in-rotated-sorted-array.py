"""
Problem: Search in rotated sorted array
Difficulty: M
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution:
    def search_wrong_soln(self, nums: List[int], target: int) -> int:
        """
        - Hmm this is interesting. so the nums array is possibly rotated at a random index. and we have to find the target value from the output. This is yet another modification-ish question on the normie binary search. 
        - What I think we'll do binary search to find out the pivot first. 
        """

        low = 0 
        high = len(nums) - 1

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        while low <= high:
            mid = ( low + high ) // 2
            if nums[mid] > nums[mid+1]:
                if (( target < nums[mid] and target > nums[0] ) or ( target == nums[mid] ) or ( target == nums[0] )):
                    print("left")
                    # target is in left sub-array.
                    low_left = 0
                    high_left = mid

                    while low_left <= high_left:
                        mid_left = ( low_left + high_left ) // 2

                        if nums[mid_left] == target:
                            return mid_left 
                        elif nums[mid_left] > target:
                            high_left = mid_left - 1 
                        else:
                            low_left = mid_left + 1 
                    return - 1

                if (( target > nums[mid+1] and target < nums[len(nums) - 1] ) or (target == nums[mid+1]) or (target == nums[len(nums)-1])):
                    print("right")
                    #target is in right sub-array. 
                    high_right = len(nums) -1 
                    low_right = mid + 1
                    
                    while low_right <= high_right:
                        mid_right = ( low_right + high_right ) // 2

                        if nums[mid_right] == target:
                            return mid_right 
                        elif nums[mid_right] > target:
                            high_right = mid_right - 1 
                        else:
                            low_right = mid_right + 1 
                    return - 1
                return -1
            
            else:
                high = mid - 1

        low = 0 
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

# My assumption that you always have to go backward, i.e in the else block just giving high = mid - 1 is wrong. Apparantly you can solve this in one loop using the standard binary search and I have no idea how that's done but we'll look at it tomorrow. 

    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition: 
        - The idea here's to work around the problem that we have / to use the end-situation resulting from the constraint put on us in the question to our own advantage. And here the advantage is that at all point, we'll have only one of the two parts sorted.
        - Now here what we're making use is to play to our strengths. What do we have here - Binary search, what is binary search good at ? searching sorted spaces - And at all point we'll have atleast one sorted space -- you sort that , you check if you've found your answer there, if not you leave that and you go to the other half. 
        - This way you can do it in one single pass. --- very interesting and it's the mental model that matters here. 
        - In my previous solution, my use of sub-loops inside was wrong. And this is because I wasn't trusting the outerloop to do it's job so I thought physically setting the boundaries like low == 0 and all was the right thing to do , but that does the opposite. I try to manually take control of the looping operation, when the algorithm started becoming complex...
        - The beauty of while low <= high: is that it is an automatic shrinking machine. You don't need to spin up a new machine to search a smaller space; you just need to feed the updated boundaries back into the main machine. It takes a while to build the intuition to just say low = mid + 1 and let the while loop take the wheel on the next pass.
        - My initial comments perfectly captured my first thought process: "We'll do binary search to find out the pivot first." Because we mentally split the problem into two distinct tasks (Task A: Find the sorted half, Task B: Search for the target), our brain naturally wanted to write two distinct loops. The inner loop was our way of saying, "Okay, I found the sorted part. Now let me just run a standard, safe binary search right here."

        Time Complexity: O(logn)
        Space Complexity: O(1)
        Reasoning : obv , since we're doing the iterative approach.
        """
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if target == nums[low]:
                    return low
                if target > nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target == nums[high]:
                    return high
                if target > nums[mid] and target < nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
        