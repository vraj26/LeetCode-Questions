class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #init pointers which point to start and end of list
        l, r = 0, len(nums) - 1

        #only loop through the pointers cross or are equal to each other
        while l<=r:

            #set the midpoint value to the INTEGER middle value
            m = (l+r) //2

            #if target is greater than current midpoint, then shift left pointer
            if nums[m] < target:
                l = m+1
            
            #if target is less than current midpoint, then shift right pointers
            elif nums[m] > target:
                r = m-1
            
            #return m (this means midpoint is now the target)
            else:
                return m
        
        #return -1 if tehre is no target
        return -1
              




        
