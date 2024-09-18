class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers for binary search
        l, r = 0, len(nums) - 1
        # Initialize result with the first element
        res = nums[0]

        while l <= r:
            # If the subarray is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            # Calculate the midpoint
            midpoint = (l + r) // 2

            # Update result if midpoint value is smaller
            res = min(res, nums[midpoint])

            # Decide which half to search next
            if nums[midpoint] >= nums[l]:
                # Minimum is in the right half
                l = midpoint + 1
            else:
                # Minimum is in the left half
                r = midpoint - 1

        return res
