"""
Problem: Find First and Last Position of Element in Sorted Array
Difficulty: M
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
class Solution:
    def searchRange_bruteforce(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition: The only problem here is since there is two seperate walks to the left most and right most ends, this is an O(n) solution and what we want is an O(logn) solution. And for that what's needed is for left and right walks, we have to do two seperate binary searches lmao -- See , the mental model that you have to follow is just this -- searching in an already sorted space -- ALWAYS THINK OF BINARY FUCKING SEARCH. SAY THE NAME -- BINARY FUCKING SEARCH -- THAT"S GODDAMN RIGHT!!

        Time Complexity: O(n)
        Space Complexity: O(logn) -- recursive stack size 
        Reasoning : 
        """
        def recursive_s(low, high):
            if low > high:
                return [-1, -1]
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                print(low, mid, high)
                left = mid
                right = mid
                # right walk :

                for i in range(mid+1,high+1):
                    if nums[i] != target:
                        right = i-1
                        break
                    else:
                        right = i

                
                #left walk:
                for i in range(mid-1, low-1, -1):
                    if nums[i] != target:
                        left = i+1
                        break
                    else:
                        left = i
                
                return [left, right]
            
            elif nums[mid] > target:
                return recursive_s(low, mid-1)
            else:
                return recursive_s(mid+1, high)
        
        return recursive_s(0, len(nums) - 1)
    
    def searchRange_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition: As mentioned above in the bruteforce, here's the optimal solution in terms of TC -- I want to learn the recursive intuition , hence I'm doing the recursive solution. This is not optimal in terms of SC, in terms of SC , iterative solution is optimal. 
        
        So here, the only difference is that since both the left and right halves are sorted already, we're going to do a modified version of binary search for finding the left and right values that's all. 

        Time Complexity: O(nlogn)
        Space Complexity: O(logn)
        Reasoning : obv
        """
        
        
        def mid_walk_left(low, high):
            """
            - Here what we have to do is to do binary search to figure out: 
                - first occurence of target in the left half 
                - last occurence of target in the right half. 
            - I'm thinking about the binary search how that would look in the two halves. 
            - you try to find the value and if the value is not found you can send -1 and you can use this to set the left / right value to be mid. 
            - now if you found the value to be mid then
            - Hmm this could be tricky -- trying to strip this problem down , what are we looking for here ? -- in this modified inner binary search, we're trying to find out , in the left half - if the value we find == target and if it's the first value of target and in the right half, it would be if we find == target and if it's the last value of target hmmm............ this can be translated into a constraint.. very interesting..... 
            """
            if low > high:
                return -1
            mid = ( low + high ) // 2 
            if nums[mid] == target:
                if mid == 0:
                    return mid
                if nums[mid-1] != target:
                    return mid
                else:
                    return mid_walk_left(low, mid-1)
            elif nums[mid] < target:
                return mid_walk_left(mid+1, high)
            else:
                return mid_walk_left(low, mid-1)
            
        def mid_walk_right(low, high):
            if low>high:
                return -1 
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                if mid == len(nums) -1:
                    return mid
                if nums[mid+1] != target:
                    return mid
                else:
                    return mid_walk_right(mid+1, high)

            elif nums[mid] < target:
                return mid_walk_right(mid+1, high)
            else:
                return mid_walk_right(low, mid-1)

        def recursive_s(low, high):
            if low > high:
                return [-1, -1]
            
            mid = ( low + high ) // 2

            if nums[mid] == target:
                left = mid_walk_left(low, mid-1)
                right = mid_walk_right(mid+1, high)

                if left == -1 :
                    left = mid
                
                if right == -1:
                    right = mid
                
                return [left, right]
            
            elif nums[mid] > target:
                return recursive_s(low, mid-1)
            else:
                return recursive_s(mid+1, high)
        
        return recursive_s(0, len(nums) - 1)
    